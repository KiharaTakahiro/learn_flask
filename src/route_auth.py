""" 認証が必要なルート定義用モジュール
    
  メソッドコメントは常に書きたいがroute定義用のファイル
  であることを強調したいため本モジュール内はあえてメソッドコメントは記載しない
  モジュール内は画面ごとに記載し、画面をまたぐルートの前にどの画面用のルートかを
  記載する

  route名規則:
    /(画面用ルート)/(アクション)
      例) /login/index
    ※ 画面用ルートは画面ごとに統一するルール
    ※ アクションについては別途規則を記載する

  アクション名規則: 
    index:    初期表示
    search:   検索処理
    update:   データの更新系処理
    register: 新規データ作成系処理
    ※ 上記以外で処理が特殊な場合は固有の名前をつけるのは良いが当てはまる場合は規則に従う
    ※ 同一画面で同一のアクションがある場合は(アクション名規則)_(対象名)で記載する
    例) update_users
  
  メソッド名規則:
    (画面用ルート)_(アクション)
"""
from flask import Flask, render_template, request, Blueprint, redirect, url_for, g
from src.models.user import find_user_for_auth

app_route_auth = Blueprint('app_route_auth', __name__)

@app_route_auth.before_request()
def load_user():
  """ ユーザの認証を確認する

      格納されている認証Keyと有効期限が一致するユーザをユーザ情報に設定する
      上記のルールで認証に失敗しているケースではログイン画面に遷移させる

  """

  # 認証キーがない場合はログイン画面に遷移
  if session['auth_key'] is None
    return redirect(url_for('login.index'))
  
  # ユーザを取得
  user = find_user_for_auth(session['auth_key'])

  # ユーザを取得できない場合は期限切れか不正ユーザと判断してログイン画面に遷移させる
  if user is None
    return redirect(url_for('login.index'))

  g.user = user



# メニュー画面
@app_route_auth.route('/menu/index')
def menu_index():
  return render_template('menu.html', title='MENU')

# パスワードリセット画面
@app_route_auth.route('/password/index')
def password_index():
  return render_template('password.html', title='PASSWORD')

# ユーザマスタ画面
@app_route_auth.route('/user_master/index')
def user_master_index():
  users = find_all_users()
  return render_template('user_master.html', title='USER MASTER')
