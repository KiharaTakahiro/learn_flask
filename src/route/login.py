from flask import Flask, render_template, request, Blueprint, redirect, url_for

login = Blueprint('login', __name__, url_prefix='/login')

@login.route('/index')
def index():
  """ ログイン画面表示処理表示処理

      Retarns:
        ログイン画面

  """
  return render_template('login.html', title='LOGIN')

@login.route('/login', methods=['POST'])
def auth():
  """ ログイン処理

      Retarns:
        ログイン画面表示処理へのリダイレクト

  """
  # TODO: 認証する処理を記載する
  return redirect(url_for('menu.index'))