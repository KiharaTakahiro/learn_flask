import psycopg2
from src.infra.db_connector import DbConnector

def find_all_users():
    db = DbConnector.get_instance()
    users = db.find('SELECT * FROM users;')
    return users