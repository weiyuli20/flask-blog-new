''' 工厂模式创建APP'''

import os
from flask import Flask
from .config import config
from .extensions import db,migrate
from .auth import bp as auth_bp




def create_app(config_name =None):
    app = Flask(__name__)
    configure_app(app, config_name)
    configure_extensions(app)
    configure_blueprints(app)
    return app



def configure_app(app, config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    if config_name in config:
        app.config.from_object(config[config_name])

def configure_extensions(app):
    # 注册数据库连接
    db.init_app(app)
    # Init Flask-Migrate
    migrate.init_app(app, db)

def configure_blueprints(app):
    '''
    注册蓝图
    '''
    app.register_blueprint(auth_bp, url_prefix='/auth')





from . import models