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


def insert(con,login,summ, promo, operId):
    current_date = datetime.now()
    query = f"insert into wallet.order (`login`,`summa`,`date`,`OperationId`,`PaymentState`,`promo`) values ('{login}', {summ},'{current_date}','{operId}',0, {promo});"

    with con.cursor() as cursor:
        cursor.execute(query)
        con.commit()

def select_last_oper(con,past_time):
    query = f"SELECT * FROM wallet.order where date >= DATE_SUB(NOW() , INTERVAL {past_time} MINUTE);"

    with con.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        con.commit()
        list_oper_id = []
        for i in result:
            list_oper_id.append(i['OperationId'])
        return list_oper_id


