from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from steamget.order_f import QiwiForm

def index(request):
    return render(request,"index.html")


def results(request,name,age):

    results = f"<p>1){name}</p><p>2){age}</p>"

    return HttpResponse(results)

def order(request):
    mpost = request.POST.get("login",0)
    money = request.POST.get("money",0)
    promo = request.POST.get("promo",0)
    results = f"""
        <h3>{mpost}</h3>
        <h3>{money}</h3>
        <h3>{promo}</h3>
    """
    print(money)
    if not money:
        return HttpResponsePermanentRedirect("/")

    request1 = QiwiForm(money)
    request1.createSignHash()
    url = request1.qiwi_request()

    return HttpResponsePermanentRedirect(url)

