from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import JsonResponse
from steamget.order_f import QiwiForm
from steamget.worksql import *
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",format="%(asctime)s %(levelname)s %(message)s")

bdname = "wallet"
userbd = "root"
passwordbd = "root"

def index(request):
    try:
        ObSql = workSql(bdname, "localhost", userbd, passwordbd)
        count = ObSql.select_counts_paid()
    except Exception as e:
        count = 0
        logging.warning("sql" + str(e))

    count_user = 2104 + count
    data ={"count_user": count_user}
    return render(request,"index.html", context=data)

#Qazwsxedcf1-\u2036283_ashibur\u2036283_wallet
def results(request):
    try:
        ObSql = workSql(bdname, "localhost", userbd, passwordbd)
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
        ObSql = workSql(bdname, "localhost", userbd, passwordbd)
        coef, id_promo = ObSql.promo_for_login(login,promo)
        print(coef)
    except Exception as e:
        logging.warning("sql" + str(e))

    try:
        steam_money = money
        money = round(int(money) * (1 + coef), 2)
        print(money)
        if len(login) <= 0:
            return HttpResponsePermanentRedirect("/")
    except Exception as e:
        logging.warning(str(e))
        return HttpResponsePermanentRedirect("/")


    try: # ошибка на стороне платежки(1 раз словил)
        request1 = QiwiForm(str( ))
        request1.createSignHash()
        url, orderId = request1.qiwi_request()
    except Exception as e:
        logging.warning(str(e))
        return HttpResponsePermanentRedirect("/")

    try:
        ObSql.insert(login, money, id_promo, orderId)

    except Exception as e:
        logging.warning("sql" + str(e))


    return HttpResponsePermanentRedirect(url)


def coificent_check_promo(request):
    promo_label = request.GET.get("promo", 0)
    try:
        ObSql = workSql(bdname, "localhost", userbd, passwordbd)
        coef, id_promo = ObSql.promo_for_login("111", promo_label)# можно и логин приписать норм
    except Exception as e:
        logging.warning("sql" + str(e))

    return JsonResponse({'coef':coef})