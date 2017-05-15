#！/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer,CHAR,VARCHAR,ForeignKey,Index,DateTime,DECIMAL,TEXT
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/jddb?charset=utf8',max_overflow=5)
Base = declarative_base()

class Province(Base):
    '''省'''
    __tablename__ = 'province'
    nid = Column(Integer,primary_key=True)
    caption = Column(VARCHAR(16),index=True)
class City(Base):
    '''
    市
    '''
    __tablename__ = 'city'
    nid = Column(Integer,primary_key=True)
    caption = Column(VARCHAR(16),index=True)
    province_id = Column(Integer,ForeignKey('province.nid'))
class County(Base):
    '''县（区）'''
    __tablename__ = 'county'
    nid = Column(Integer,primary_key=True)
    caption = Column(VARCHAR(16),index=True)
    city_id = Column(Integer,ForeignKey('city.nid'))

class Userinfo(Base):
    '''用户信息'''
    __tablename__ = 'userinfo'
    nid = Column(Integer, primary_key=True)
    USER_TYPE=(
        {'nid': 1, 'caption': '用户'},
        {'nid': 2, 'caption': '商户'},
        {'nid': 3, 'caption': '管理员'},
    )
    user_type = Column(Integer)
    VIP_TYPE = (
        {'nid': 1, 'caption': '铜牌'},
        {'nid': 2, 'caption': '银牌'},
        {'nid': 3, 'caption': '金牌'},
        {'nid': 4, 'caption': '铂金'},
    )
    vip = Column(Integer)
    username = Column(VARCHAR(32))
    password = Column(VARCHAR(64))
    email = Column(VARCHAR(64))
    last_login = Column(DateTime)
    ctime = Column(DateTime)
    __table_args__=(
        Index('ix_user_pwd','username','password'),
        Index('ix_email_pwd', 'email', 'password'),
    )

class Merchant(Base):
    '''商户'''
    __tablename__ = 'merchant'
    nid = Column(Integer, primary_key=True)
    domain = Column(CHAR(8),index=True)
    business_mobile =Column(CHAR(11))
    qq =Column(CHAR(16))
    backend_mobile = Column(CHAR(16))
    county_id = Column(Integer,ForeignKey('county.nid'))
    user_id = Column(Integer, ForeignKey('userinfo.nid'))

    name = Column(VARCHAR(64),index=True)
    business_phone = Column(VARCHAR(16))
    backend_phone = Column(VARCHAR(16))
    address = Column(VARCHAR(128))

#Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)