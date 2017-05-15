#！/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 调用协调者
        self.write("Hello, world")
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        # 调用协调者
        self.write("Hello, world")
    def post(self, *args, **kwargs):
        user = 'alex'
        pwd = '123'
        from Models.User import UserSevice
        from Repository.UserRepository import UserRepository
        service = UserSevice()
        obj = service.check_login(user=user,email=None,pwd=pwd)
        # obj 封装用户所有信息
        print(obj.username)
        print(obj.email)
        print(obj.vip_obj.nid)
        print(obj.vip_obj.caption)