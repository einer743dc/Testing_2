from django.http import request,HttpResponse
from django.shortcuts import render
from django.template import Context,Template


def test_1(request,name):
    return HttpResponse(f'Hey you in! {name}')

def testing_template(request):
    frutas = {
        'pera' : 300,
        'mango' : 500,
        'banano' : 200,
    }
    contexto = {'frutas':frutas}
    return render(request,'index_1.html',context=contexto)