import pymysql


def create_or_open_db():
    db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS TEST")

    # 使用预处理语句创建表
    sql = '''CREATE TABLE TEST (_ID INT,
              GOOD_ID CHAR(20) )'''

    cursor.execute(sql)
    db.close()


if __name__ == "__main__":
    create_or_open_db()
