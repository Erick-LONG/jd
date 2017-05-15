#！/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
from UIAdmin.Controllers import Account
from UIAdmin.Controllers import Home
from UIAdmin.Controllers import Region
import BootMapper
settings = {
    'static_path':'Static',
    'static_url_prefix':'/Static/',
    'template_path':'Views',
}
application = tornado.web.Application([
    (r"/index$", Home.IndexHandler),
    (r"/login$", Account.LoginHandler),
    (r"/province_data$", Region.ProvinceDataHandler),
    (r"/ProvinceManager.html$", Region.ProvinceManagerHandler),  #省份模板展示
    (r"/province.html$", Region.ProvinceHandler), #省份的增删改查
    (r"/CityManager.html$", Region.CityManagerHandler), #市模板展示
    (r"/City.html$", Region.CityHandler),#市的增删改查
    (r"/CountryManager.html$", Region.CountyManagerHandler), #县的模板展示
    (r"/Country.html$", Region.CountyHandler), #县的增删改查
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()