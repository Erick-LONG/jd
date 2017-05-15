#！/usr/bin/env python
# -*- coding:utf-8 -*-

# 4、
# 实现业务接口
# 具体SQL语句
from Models.User import IUserRepository
from Repository.DBconnection import Dbconnection
from Models.User import UserModel
from Models.User import VipModel
from Models.User import UserTypeModel
class UserRepository(IUserRepository):
    def __init__(self):
        self.db_conn = Dbconnection()
    def fetch_one_by_user_pwd(self,email,pwd):
        ret = None
        cursor = self.db_conn.conncet()
        sql='''select nid,username,email,last_login,vip,user_type from Userinfo where email=%s and password=%s '''
        cursor.execute(sql,(email,pwd))
        db_result = cursor.fetchone()
        self.db_conn.close()
        if db_result:
            # 将字典转化为对象
            obj = UserModel(
                nid=db_result['nid'],
                username=db_result['username'],
                email=db_result['email'],
                last_login=db_result['last_login'],
                vip_obj=VipModel(nid=db_result['vip_obj']),
                user_type_obj=UserTypeModel(nid=db_result['user_type_obj']),
            )
            return obj
        return db_result

    def fetch_one_by_email_pwd(self,user,pwd):
        # 自己拼接SQL语句
        pass