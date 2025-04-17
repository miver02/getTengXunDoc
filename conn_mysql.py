import pymysql
from config import *

class connMysql:
    def __init__(self, host, port, user, password, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db, charset=self.charset)
            self.cursor = self.conn.cursor()
            print(f"数据库连接成功")
        except Exception as e:
            print(f"数据库连接失败: {e}")


    def close(self):
        self.conn.close()
        self.cursor.close()

    def execute(self, sql, params=None):
        try:
            self.cursor.executemany(sql, params)
            # self.conn.commit()
            print(f"数据插入成功")
        except Exception as e:
            print(f"数据插入失败: {e}")


def main(params):
    conn_mysql = connMysql(host, port, user, password, db, charset)
    conn_mysql.connect()
    sql = 'insert into douyin_creators (id, wechat_nickname, creator_nickname, level, followers, avg_plays, homepage_url, contact_info, price_info, create_time, update_time) \
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    conn_mysql.execute(sql, params)
    conn_mysql.close()

if __name__ == '__main__':
    conn_mysql = connMysql(host, port, user, password, db, charset)
    conn_mysql.connect()


