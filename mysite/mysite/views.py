from django.http import HttpResponse
from django.shortcuts import render_to_response

def here(request):
    return HttpResponse('媽，我在這！')

def math(request, a, b):
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    return render_to_response('math.html',locals())

def menu(request):
    food1 = { 'name':'番茄炒蛋', 'price':60, 'comment':'好吃', 'is_spicy':False }
    food2 = { 'name':'蒜泥白肉', 'price':100, 'comment':'人氣推薦', 'is_spicy':True }
    foods = [food1,food2]   #[]內都沒放東西就會顯示餐廳沒賣食物
    return render_to_response('menu.html',locals())