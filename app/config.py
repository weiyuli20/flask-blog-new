#config.py
 
# -*- coding: utf-8 -*-
import os
 
class BaseConfig:
    # 获取当前文件所在目录的绝对路径
    basedir = os.path.abspath(os.path.dirname(__file__))
    # 数据库默认配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 密钥用于会话管理等
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

class DevelopmentConfig(BaseConfig):
    # 开发环境开启调试模式
    DEBUG = True
    # 开发环境使用的数据库
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BaseConfig.basedir, 'development.db')

class TestingConfig(BaseConfig):
    # 测试环境开启测试模式
    TESTING = True
    # 测试环境使用的数据库
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BaseConfig.basedir, 'testing.db')
    # 禁用 CSRF 保护
    WTF_CSRF_ENABLED = False

class ProductionConfig(BaseConfig):
    # 生产环境关闭调试模式
    DEBUG = False
    # 生产环境使用的数据库，可从环境变量获取
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BaseConfig.basedir, 'production.db')
 
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}