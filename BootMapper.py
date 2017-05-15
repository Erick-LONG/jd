#！/usr/bin/env python
# -*- coding:utf-8 -*-
from Infrastructure.DI import Mapper
from Models.User import UserSevice
from Repository.UserRepository import UserRepository
Mapper.register(UserSevice,UserRepository())
