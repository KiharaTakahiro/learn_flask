from flask import Flask, render_template, request, Blueprint, redirect, url_for

login = Blueprint('login', __name__, url_prefix='/login')

# ログイン画面表示処理
@login.route('/index')
def index():
  return render_template('login.html', title='LOGIN')

# ログイン処理
@login.route('/login', methods=['POST'])
def auth():
  # TODO: 認証する処理を記載する
  return redirect(url_for('menu.index'))