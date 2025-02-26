from flask import Blueprint

bp = Blueprint('auth', __name__)  #定义蓝图

from . import routes