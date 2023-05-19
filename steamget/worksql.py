import pymysql.cursors

from datetime import datetime



class workSql():
    def __init__(self,bd_name,host,user,password):
        self.bd_name = bd_name
        self.host = host
        self.user = user
        self.password = password
        self.con = self.connect_mysql()
        self.base_coef = self.select_promo('base')['coefficient']

    def connect_mysql(self):
        return pymysql.connect(host=self.host,
                               port=3306,
                               user=self.user,
                               password=self.password,
                               db=self.bd_name,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)


    def insert(self,login,summ, promo, operId):
        current_date = datetime.now()
        query = f"insert into {self.bd_name}.order (`login`,`summa`,`date`,`OperationId`,`PaymentState`,`promo`) values ('{login}', {summ},'{current_date}','{operId}','Created', {promo});"

        with self.con.cursor() as cursor:
            cursor.execute(query)
            self.con.commit()

    def select_last_oper(self,past_time):
        query = f"SELECT * FROM {self.bd_name}.order where date >= DATE_SUB(NOW() , INTERVAL {past_time} MINUTE) and PaymentState = 'Created';"

        with self.con.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            self.con.commit()
            list_oper_id = []
            for i in result:
                list_oper_id.append(i['OperationId'])
            return list_oper_id

    def select_counts_paid(self):
        query = f"SELECT count(PaymentState) as count FROM  {self.bd_name}.order where PaymentState = 'paid' ;"
        with self.con.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            self.con.commit()
        try:  # если такого нету
            return result[0]['count']
        except:
            return 0

    def update_status(self,status,oper_id):
        query = f"UPDATE `{self.bd_name}`.`order` SET `PaymentState` = '{status}' WHERE (`OperationId` = '{oper_id}');"
        with self.con.cursor() as cursor:
            cursor.execute(query)
            self.con.commit()
#это говно надо в функцию\процедуру объeденить sql!!!!!!!!!!!!!!!!!!!!!!
#это говно надо в функцию\процедуру объeденить sql!!!!!!!!!!!!!!!!!!!!!!

    def promo_for_login(self, login, label):
        promo = self.select_promo(label)
        if promo:
            print(promo)
            query = f"SELECT count(login) as count from {self.bd_name}.order where promo = {promo['id_promo']} and PaymentState = 'paid' and login = '{login}';"
            with self.con.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                self.con.commit()

            if result[0]['count'] < promo['counts_use_for_user']:
                return promo['coefficient'], promo['id_promo']
            else:# исчерпал лимит
                return self.base_coef, 0
        else:# ошибка промика, такого нет
            return self.base_coef, 0


    def select_promo(self, label):#только если есть и включен
        query = f"SELECT * FROM {self.bd_name}.tpromo where label = '{label}' and turned = 1 and end_data >= NOW();"
        with self.con.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            self.con.commit()
            try:#если такого нету
                return result[0]
            except:
                return 0

#
# new = workSql("wallet","localhost", "root", "root")
# print(new.promo_for_login('er','youasda'))