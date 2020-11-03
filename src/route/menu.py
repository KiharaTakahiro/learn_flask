from flask import Flask, render_template, request, Blueprint

menu = Blueprint('menu', __name__, url_prefix='/menu')

# メニュー画面表示処理
@menu.route('/index')
def index():
  return render_template('menu.html', title='MENU')