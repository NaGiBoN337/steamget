from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from steamget.order_f import QiwiForm
from steamget.worksql import *


def index(request):
    return render(request,"index.html")


def results(request):

    results = f""

    return HttpResponse(results)

def order(request):
    login = request.POST.get("login",0)
    money = request.POST.get("money",0)
    promo = request.POST.get("promo",0)

    try:
        money = int(money)
        if len(login) <= 0:
            return HttpResponsePermanentRedirect("/")
    except:
        return HttpResponsePermanentRedirect("/")


    request1 = QiwiForm(str(money))
    request1.createSignHash()
    url, OperId = request1.qiwi_request()

    try:
        connection = connect_mysql("localhost", "root", "root", "wallet")
        insert(connection,login, money, 0, OperId)

    except Exception as e:
        print(e)

    return HttpResponsePermanentRedirect(url)

