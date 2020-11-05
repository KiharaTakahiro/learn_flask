import psycopg2.pool

class DbConnector():
    _unique_instance = None
    _connection_pool = None
    def __new__(cls):
        raise NotImplementedError('コンストラクタの直接呼び出しは行わない')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if cls._unique_instance is None:
            cls._unique_instance = cls.__internal_new__()
        return cls._unique_instance

    def __get_connect(self):
        if self._connection_pool is None:
            self._connection_pool = psycopg2.pool.SimpleConnectionPool(minconn=2, maxconn=5, database="learn_flask", user="postgres", password="Madb45pk", host="localhost")
        return self._connection_pool.getconn()

    def find(self, sql, params=[], time_out=1000):
        try:
            con = self.__get_connect() 
            cur = con.cursor()   
            cur.execute(f'SET statement_timeout TO {time_out}')
            cur.execute(sql, params)
            results = cur.fetchall()
            cur.close()
            return results
        except QueryCanceledError as err:
            # TODO: 発生したエラーをログ出力する予定
            print(err)