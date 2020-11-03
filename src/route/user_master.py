from flask import Flask, render_template, request, Blueprint

user_master = Blueprint('user_master', __name__, url_prefix='/user_master')

# ユーザマスタ画面表示処理
@user_master.route('/index')
def index():
  return render_template('user_master.html', title='USER MASTER')
