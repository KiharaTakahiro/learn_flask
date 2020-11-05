from flask import Flask, render_template, request, Blueprint

password = Blueprint('password', __name__, url_prefix='/password')

@password.route('/index')
def index():
  """ パスワードリセット画面表示処理

      Retarns:
        パスワードリセット画面

  """
  return render_template('password.html', title='PASSWORD')