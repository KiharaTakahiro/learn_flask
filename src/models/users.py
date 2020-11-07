import psycopg2
import datetime
from src.infra.db_connector import DbConnector

def find_all_users():
  """ ユーザテーブルから全件取得

    Retarns:
      ユーザテーブルからの取得結果
  """
  db = DbConnector.get_instance()
  users = db.find('SELECT * FROM users;')
  return users

def find_user_for_auth(auth_key):
  """ 認証用のユーザ情報を取得

    認証キーをもとにユーザ情報を返却

    Retarns:
      認証キーに紐付くユーザ情報を返却
  """
  db = DbConnector.get_instance()
  today = datetime.date.today()
  user = db.find('SELECT * FROM users where auth_key = %s and auth_dead_line <= %s;',(auth_key,today.strftime('%Y%m%d')))
  return user
