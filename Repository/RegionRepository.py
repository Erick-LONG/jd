#！/usr/bin/env python
# -*- coding:utf-8 -*-
# 4、
# 实现业务接口
# 具体SQL语句
from Repository.DBconnection import Dbconnection
from Models.Region import IRegionRepository

class RegionRepository(IRegionRepository):
    def __init__(self):
        self.db_conn = Dbconnection()  # 实例化数据库链接对象（只需创建一次对象，下面所有方法都不需要再创建）

    def fetch_province(self):  # 获取所有省份
        cursor = self.db_conn.conncet()
        sql = """select nid,caption from province order by nid desc """
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_province_by_page(self, start, offset):  # 根据分页获取省份
        ret = None
        cursor = self.db_conn.conncet()
        sql = """select nid,caption from province order by nid desc limit %s offset %s """
        cursor.execute(sql, (offset, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_province_count(self):  # 获取省份总数
        cursor = self.db_conn.conncet()
        sql = """select count(1) as count from province """
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def exist_province(self, caption):  # 省份是否存在
        cursor = self.db_conn.conncet()
        sql = """select count(1) as count from province where caption=%s """
        cursor.execute(sql, (caption,))
        db_result = cursor.fetchone()
        self.db_conn.close()

        return db_result['count']

    def add_province(self, caption): # 创建省份
        cursor = self.db_conn.conncet()
        sql = """insert into province (caption) values(%s)"""
        effect_rows = cursor.execute(sql, (caption,))
        self.db_conn.close()
        return effect_rows

    def update_province(self, nid, caption):  # 更新省份
        cursor = self.db_conn.conncet()
        sql = """update province set caption=%s where nid=%s """
        effect_rows = cursor.execute(sql, (caption, nid,))
        self.db_conn.close()
        return effect_rows

    def remove_province(self, nid):
        cursor = self.db_conn.conncet()
        sql = """delete from province where nid=%s """
        effect_rows = cursor.execute(sql, (nid,))
        self.db_conn.close()
        return effect_rows
    def fetch_city_by_province(self,province_id):
        cursor = self.db_conn.conncet()
        sql = """select nid,caption from city where province_id=%s """
        cursor.execute(sql, (province_id,))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_city_count(self):
        cursor = self.db_conn.conncet()
        sql = """select count(1) as count from city """
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']
    def fetch_city_by_page(self,offset, start):
        ret = None
        cursor = self.db_conn.conncet()
        sql = """select
                 city.nid as nid,
                 city.caption as caption,
                 province.caption as province,
                 city.province_id as province_id
                 from city
                 left join province on city.province_id = province.nid
                 order by city.nid desc
                 limit %s offset %s """
        # sql = 'select nid,caption from province order by nid desc limit %s offset %s'
        cursor.execute(sql, (offset, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def exist_city(self, caption):  # 省份是否存在
        cursor = self.db_conn.conncet()
        sql = """select count(1) as count from city where caption=%s """
        cursor.execute(sql, (caption,))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']
    def add_city(self, caption,province_id): # 创建城市
        cursor = self.db_conn.conncet()
        sql = """insert into city (caption,province_id) values(%s,%s)"""
        effect_rows = cursor.execute(sql, (caption,province_id))
        self.db_conn.close()
        return effect_rows
    def remove_city(self, nid):
        cursor = self.db_conn.conncet()
        sql = """delete from city where nid=%s """
        effect_rows = cursor.execute(sql, (nid,))
        self.db_conn.close()
        return effect_rows
    def update_city(self, nid, caption,province_id):  # 更新城市
        cursor = self.db_conn.conncet()
        sql = """update city set caption=%s,province_id=%s where nid=%s """
        effect_rows = cursor.execute(sql, (caption, province_id,nid))
        self.db_conn.close()
        return effect_rows
    def exist_country(self, caption):  # 县是否存在
        cursor = self.db_conn.conncet()
        sql = """select count(1) as count from county where caption=%s """
        cursor.execute(sql, (caption,))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']
    def add_country(self, caption,city_id): # 创建县
        cursor = self.db_conn.conncet()
        sql = """insert into county (caption,city_id) values(%s,%s)"""
        effect_rows = cursor.execute(sql, (caption,city_id))
        self.db_conn.close()
        return effect_rows
    def fetch_country_count(self):
        cursor = self.db_conn.conncet()
        sql = """select count(1) as count from county """
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']
    def fetch_country_by_page(self,offset, start):
        ret = None
        cursor = self.db_conn.conncet()
        sql = """select
                 county.nid as nid,
                 county.caption as caption,
                 city.nid as city_nid,
                 city.caption as city_caption,
                 province.caption as province,
                 city.province_id as province_id
                 from county
                 left join city on county.city_id = city.nid
                 left join province on city.province_id = province.nid
                 order by county.nid desc
                 limit %s offset %s """
        cursor.execute(sql, (offset, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result