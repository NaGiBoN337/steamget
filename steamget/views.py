from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from steamget.order_f import QiwiForm
from steamget.worksql import *
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",format="%(asctime)s %(levelname)s %(message)s")

def index(request):
    return render(request,"index.html")

#Qazwsxedcf1-\u2036283_Ashibur\u2036283_wallet
def results(request):
    try:
        ObSql = workSql("wallet", "localhost", "root", "root")
        ObSql.select_last_oper(20)
        request1 = QiwiForm("1")
        print(list_oper_created)
        for i in list_oper_created:
            if request1.checkPay(i):
                ObSql.update_status("paid",i)
            else:
                pass

    except Exception as e:
        logging.warning("sql" + str(e))
        print(e)

    return HttpResponsePermanentRedirect("/")
    #return HttpResponse("<h2>ошибка:   </h2>")
   # return HttpResponse(results)

def order(request):#
    login = request.POST.get("login",0)
    money = request.POST.get("money",0)
    promo = request.POST.get("promo",'base')

    try:
        ObSql = workSql("wallet", "localhost", "root", "root")
        coef = ObSql.promo_for_login(login,promo)
        print(coef)
    except Exception as e:
        logging.warning("sql" + str(e))

    try:
        money = round(int(money) * (1 + coef),2)
        print(money)
        if len(login) <= 0:
            return HttpResponsePermanentRedirect("/")
    except:
        return HttpResponsePermanentRedirect("/")


    try: # ошибка на стороне платежки(1 раз словил)
        request1 = QiwiForm(str(money))
        request1.createSignHash()
        url, orderId = request1.qiwi_request()
    except:
        return HttpResponsePermanentRedirect("/")

    try:
        ObSql.insert(login, money, 0, orderId)

    except Exception as e:
        logging.warning("sql" + str(e))


    return HttpResponsePermanentRedirect(url)

