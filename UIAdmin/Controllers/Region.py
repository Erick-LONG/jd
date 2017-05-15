#！/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import json
from Models.Region import RegionService
from Repository.RegionRepository import RegionRepository
class ProvinceHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """
        获取
        :param args:
        :param kwargs:
        :return:
        """
        if self.get_argument('type', None) == 'all':  # 如果是获取所有数据
            ret = {'status': True, 'rows': "", 'summary': ''} # 将来要返回给前端的字典，包含是否获取成功的状态、获取的数据、错误信息
            try:
                region_service = RegionService(RegionRepository()) # 将数据库处理类的对象传入数据库业务协调类
                all_province_list = region_service.get_province()  # 获取所有省份
                ret['rows'] = all_province_list  # 将省份数据添加进返回前端的字典
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)
            self.write(json.dumps(ret))  # 返回给前端
        else:
            # 如果是获取分页数据
            ret = {'status': True, 'total': 0, 'rows': [], 'summary': ''}
            try:
                rows = int(self.get_argument('rows', 10))  # 每页显示10条
                page = int(self.get_argument('page', 1))  # 显示第一页
                start = (page - 1) * rows
                #开始条数

                region_service = RegionService(RegionRepository())
                row_list = region_service.get_province_by_page(start, rows)  # 根据分页获取省份数据
                row_count = region_service.get_province_count() # 获取省份总数

                ret['total'] = row_count
                ret['rows'] = row_list
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)

            self.write(json.dumps(ret))  # 返回给前端

    def post(self, *args, **kwargs):
        """
        添加
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}
        caption = self.get_argument('caption', None)
        if not caption:
            ret['summary'] = '省份不能为空'
        else:
            try:

                region_service = RegionService(RegionRepository())
                result = region_service.create_province(caption)  # 创建省份，如果省份已存在，返回None
                if not result:
                    ret['summary'] = '省份已经存在'
                else:
                    ret['status'] = True  # 操作成功
            except Exception as e:
                ret['summary'] = str(e)

        self.write(json.dumps(ret))  # 返回给前端

    def put(self, *args, **kwargs):
        """
        更新
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}
        nid = self.get_argument('nid', None)
        caption = self.get_argument('caption', None)
        if not caption or not nid:
            ret['summary'] = '省份不能为空'
        else:
            try:

                region_service = RegionService(RegionRepository())
                result = region_service.modify_province(nid, caption)

                if not result:
                    ret['summary'] = '省份已经存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        """
        删除
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}

        nid = self.get_argument('nid', None)

        if not nid:
            ret['summary'] = '请选择要删除的省份'
        else:
            # 调用service去删除吧...
            # 如果删除失败，则显示错误信息
            try:
                region_service = RegionService(RegionRepository())
                region_service.delete_province(nid)  # 根据nid删除省份
                ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

class ProvinceDataHandler(tornado.web.RequestHandler):
    def get(self):
        # 调用协调者
        # 获取所有数据，存放到列表
        total = 98
        all_list=[]
        for item in range(total):
            temp = {'nid':item,'caption':'省'+str(item)}
            all_list.append(temp)
        # page:1
        # rows:10 # 0 10
        # page:2
        # rows:10 # 10 20
        # 获取前端请求分页信息
        page = int(self.get_argument('page',1))
        rows = int(self.get_argument('rows',10))
        # 计算分页开始和结束
        start = (page-1)*rows
        end = page*rows
        data_list = all_list[start:end]
        # 返回切片好的数据
        ret = {'total': total, 'rows': data_list}
        self.write(json.dumps(ret))
        #self.render("province.html")

class ProvinceManagerHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        # 打开页面显示所有的省
        self.render("Region/ProvinceManager.html")
class CityManagerHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        # 调用协调者
        self.render("Region/CityManager.html")

class CityHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """
        获取
        :param args:
        :param kwargs:
        :return:
        """
        if self.get_argument('type', None) == 'province':  # 如果是获取省份所有数据
            ret = {'status': True, 'rows': "", 'summary': ''} # 将来要返回给前端的字典，包含是否获取成功的状态、获取的数据、错误信息
            try:
                province_id = self.get_argument('province_id',None)
                if not province_id:
                    ret['status'] = False
                    ret['summary'] = '请指定省份ID'
                else:
                    region_service = RegionService(RegionRepository()) # 将数据库处理类的对象传入数据库业务协调类
                    rows = region_service.get_city_by_province(province_id)  # 获取所有省份
                    ret['rows'] = rows  # 将省份数据添加进返回前端的字典
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)
            self.write(json.dumps(ret))  # 返回给前端
        else:
            #如果是获取分页数据
            ret = {'status': True, 'total': 0, 'rows': [], 'summary': ''}
            try:
                rows = int(self.get_argument('rows', 10))  # 每页显示10条
                page = int(self.get_argument('page', 1))  # 显示第一页
                start = (page - 1) * rows
                #开始条数
                region_service = RegionService(RegionRepository())
                row_list = region_service.get_city_by_page(rows, start)  # 根据分页获取城市数据
                row_count = region_service.get_city_count() # 获取城市总数

                ret['total'] = row_count
                ret['rows'] = row_list
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)

            self.write(json.dumps(ret))  # 返回给前端

    def post(self, *args, **kwargs):
        """
        添加
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}
        caption = self.get_argument('caption', None)
        province_id = self.get_argument('province_id', None)
        if not caption:
            ret['summary'] = '城市不能为空'
        else:
            try:

                region_service = RegionService(RegionRepository())
                result = region_service.create_city(caption,province_id)  # 创建城市，如果城市已存在，返回None
                if not result:
                    ret['summary'] = '城市已经存在'
                else:
                    ret['status'] = True  # 操作成功
            except Exception as e:
                ret['summary'] = str(e)

        self.write(json.dumps(ret))  # 返回给前端

    def put(self, *args, **kwargs):
        """
        更新
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}
        nid = self.get_argument('nid', None)
        caption = self.get_argument('caption', None)
        province_id = self.get_argument('province_id',None)
        if not caption or not nid:
            ret['summary'] = '城市不能为空'
        else:
            try:

                region_service = RegionService(RegionRepository())
                result = region_service.modify_city(nid, caption,province_id)

                if not result:
                    ret['summary'] = '城市已经存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        """
        删除
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}

        nid = self.get_argument('nid', None)

        if not nid:
            ret['summary'] = '请选择要删除的省份'
        else:
            # 调用service去删除吧...
            # 如果删除失败，则显示错误信息
            try:
                region_service = RegionService(RegionRepository())
                region_service.delete_city(nid)  # 根据nid删除省份
                ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))
class CountyManagerHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        # 调用协调者
        self.render("Region/CountryManager.html")

class CountyHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """
        获取
        :param args:
        :param kwargs:
        :return:
        """

        #如果是获取分页数据
        ret = {'status': True, 'total': 0, 'rows': [], 'summary': ''}
        try:
            rows = int(self.get_argument('rows', 10))  # 每页显示10条
            page = int(self.get_argument('page', 1))  # 显示第一页
            start = (page - 1) * rows
            #开始条数
            region_service = RegionService(RegionRepository())
            row_list = region_service.get_country_by_page(rows, start)  # 根据分页获取城市数据
            row_count = region_service.get_country_count() # 获取城市总数
            ret['total'] = row_count
            ret['rows'] = row_list
        except Exception as e:
            ret['status'] = False
            ret['summary'] = str(e)

        self.write(json.dumps(ret))  # 返回给前端9*
    def post(self, *args, **kwargs):
        """
        添加
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}
        caption = self.get_argument('caption', None)
        city_id = self.get_argument('city_id',None)
        if not caption:
            ret['summary'] = '县不能为空'
        else:
            try:
                region_service = RegionService(RegionRepository())
                result = region_service.create_country(caption,city_id)  # 创建县，如果县已存在，返回None
                if not result:
                    ret['summary'] = '县已经存在'
                else:
                    ret['status'] = True  # 操作成功
            except Exception as e:
                ret['summary'] = str(e)

        self.write(json.dumps(ret))  # 返回给前端