import psycopg2.pool
import controller 

class DbConnector():
  """ DB疎通クラス

      DBへの疎通を行うクラス

      Args:
          _unique_instance(DbConnector):     DB疎通クラスのインスタンス
          _connection_pool(connection_pool): コネクションプール

  """
  _unique_instance = None
  _connection_pool = None

  def __new__(cls):
    raise NotImplementedError('コンストラクタの直接呼び出しは行わない')

  @classmethod
  def __internal_new__(cls):
    return super().__new__(cls)

  @classmethod
  def get_instance(cls):
    """ インスタンス返却用メソッド

        DB疎通クラスのインスタンスを返却する

        Retarns:
            インスタンス生成済みの場合: 生成済みのインスタンスを返却
            インスタンスが未生成の場合: 新規のインスタンスを生成して返却
    """
    if cls._unique_instance is None:
      cls._unique_instance = cls.__internal_new__()
    return cls._unique_instance

  def __get_connect(self):
    """ コネクション返却用メソッド

        コネクションプールが未生成の場合は新規でコネクションプールを生成する

        Retarns:
            コネクションプールからDBへのコネクションを返却する

    """
    if self._connection_pool is None:
      # TODO: moduleがcontrollerに依存するのはおかしい気もするのでここは見直す
      self._connection_pool = psycopg2.pool.SimpleConnectionPool(minconn=controller.app.config['DB_MIN_POOL_NUM'], maxconn=controller.app.config['DB_MAX_POOL_NUM'], database=controller.app.config['DB_DATABASE_NAME'], user=controller.app.config['DB_USER'], password=controller.app.config['DB_PASSWORD'], host=controller.app.config['DB_HOST'])
      return self._connection_pool.getconn()

  def find(self, sql, params=[], time_out=controller.app.config['DB_TIME_OUT']):
    """ SQLをもとにDBからデータを取得する

        SQLをもとにすべての結果を取得する
        大量データに関しては考慮していないので使用の場合は注意する

        Args:
            sql(string): 実行するSQLを格納する
            params:      SQLに使用するパラメタを指定する
            time_out:    タイムアウトの時間を指定する
        
    """
    try:
      with self.__get_connect() as con:
        with con.cursor() as cur:
          cur.execute(f'SET statement_timeout TO {time_out}')
          cur.execute(sql, params)
          return cur.fetchall()
    except QueryCanceledError as err:
      # TODO: 発生したエラーをログ出力する予定
      print(err)
      print(sql)
      print(params)
      raise