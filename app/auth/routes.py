from flask import render_template

from . import bp  # 从当前目录下导入使用蓝图

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return "hello"