from flask import Flask, render_template, request, Blueprint

password = Blueprint('password', __name__, url_prefix='/password')

# パスワードリセット画面表示処理
@password.route('/index')
def index():
  return render_template('password.html', title='PASSWORD')