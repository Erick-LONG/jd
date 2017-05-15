#！/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 调用协调者
        self.render("index.html")