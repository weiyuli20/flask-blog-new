''' 工厂模式创建APP'''

import os
from flask import Flask
from .config import config
from .extensions import db,migrate
from .auth import bp as auth_bp
from .main import bp as main_bp
from .models import User
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = '请先登录。'

def create_app(config_name =None):
    app = Flask(__name__)
    configure_app(app, config_name)
    configure_extensions(app)
    configure_blueprints(app)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User}

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
    login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

def configure_blueprints(app):
    '''
    注册蓝图
    '''
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)


