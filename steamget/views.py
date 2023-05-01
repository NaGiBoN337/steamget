from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
    return HttpResponse("Главная")

def results(request,name,age):

    results = f"<p>1){name}</p><p>2){age}</p>"

    return HttpResponse(results)

def vk(request):
    return HttpResponsePermanentRedirect("https://vk.com/feed")



    #return HttpResponse("Произошла ошибка", status=400, reason="Incorrect data")
