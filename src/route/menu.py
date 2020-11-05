from flask import Flask, render_template, request, Blueprint

menu = Blueprint('menu', __name__, url_prefix='/menu')

@menu.route('/index')
def index():
  """ メニュー画面表示処理

      Retarns:
        メニュー画面

  """
  return render_template('menu.html', title='MENU')