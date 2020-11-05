from flask import Flask, render_template, request, Blueprint
from src.models.users import find_all_users

user_master = Blueprint('user_master', __name__, url_prefix='/user_master')

@user_master.route('/index')
def index():
  """ ユーザマスタ画面表示処理

      Retarns:
        ユーザマスタ画面
  """
  users = find_all_users()
  return render_template('user_master.html', title='USER MASTER')
