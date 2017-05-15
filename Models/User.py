#！/usr/bin/env python
# -*- coding:utf-8 -*-
# 1、模型
from Infrastructure.DI import MetaClass
class UserTypeModel:
    USER_TYPE = (
        {'nid': 1, 'caption': '用户'},
        {'nid': 2, 'caption': '商户'},
        {'nid': 3, 'caption': '管理员'},
    )
    def __init__(self,nid):
        self.nid =nid
    @property
    def caption(self):
        for item in UserTypeModel.USER_TYPE:
            if item['nid'] ==self.nid:
                return item['caption']
class VipModel:
    VIP_TYPE = (
        {'nid': 1, 'caption': '铜牌'},
        {'nid': 2, 'caption': '银牌'},
        {'nid': 3, 'caption': '金牌'},
        {'nid': 4, 'caption': '铂金'},
    )
    def __init__(self,nid):
        self.nid =nid
    def caption(self):
        for item in VipModel.VIP_TYPE:
            if item['nid'] ==self.nid:
                return item['caption']

class UserModel:
    def __init__(self,nid,username,email,last_login,vip_obj,user_type_obj):
        self.nid = nid
        self.username = username
        self.email = email
        self.lasr_login = last_login
        self.vip_obj = vip_obj
        self.user_type_obj = user_type_obj

# 2、接口
class IUserRepository:
    def fetch_one_by_user_pwd(self,user,pwd):
        '''
        根据用户名密码获取对象
        :param user:
        :param pwd:
        :return:
        '''
    def fetch_one_by_email_pwd(self,email,pwd):
        '''
        根据邮箱密码获取对象
        :param email:
        :param pwd:
        :return:
        '''
# 3、协调者

class UserSevice(metaclass=MetaClass):
    def __init__(self,user_repository):
        '''
        :param user_repository: 数据仓库的对象
        '''
        self.user_repository = user_repository
    def check_login(self,user,email,pwd):
        if user:
            # 数据仓库执行SQL返回的字典
            m = self.user_repository.fetch_one_by_user_pwd(user,pwd)
        else:
            m = self.user_repository.fetch_one_by_email_pwd(email, pwd)
        # m是对象或者是None

        return m
