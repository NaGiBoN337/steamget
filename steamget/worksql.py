import pymysql.cursors

from datetime import datetime


def connect_mysql(host, user, password, db):
    return pymysql.connect(host=host,
                           port=3306,
                           user=user,
                           password=password,
                           db=db,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)


def insert(con,login ,summ, promo, operId):
    current_date = datetime.now()
    query = f"insert into wallet.order (`login`,`summa`,`date`,`OperationId`,`promo`) values ('{login}', {summ},'{current_date}','{operId}', {promo});"

    with con.cursor() as cursor:
        cursor.execute(query)
        con.commit()




