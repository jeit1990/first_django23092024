from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
text_all = """
    Имя: <strong>Иван</strong> <br/>
    Отчество: <strong>Петрович</strong><br/>
    Фамилия: <strong>Иванов</strong><br/>
    телефон: <strong>8-923-600-01-02</strong><br/>
    email: <strong>vasya@mail.ru</strong>
    """
items = [   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
            {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
            {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
            {"id": 7, "name": "Картофель фри" ,"quantity":0},
            {"id": 8, "name": "Кепка" ,"quantity":124},]
def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Носик Л.С.</i>
    """
    return HttpResponse(text)

def about(request):

    return HttpResponse(text_all)

def item(request, id):
    text = ""
    flag = 0
    for i in items:
        if i["id"] == id:
            text = f'Наименование: {i["name"]}, количество: {i["quantity"]}'
            text = text + f'<br/><a href="/items">назад к списку товаров</a>'
            flag = 1
            break
    if flag == 0:
        text = f'Товар с id={id} не найден'
    return HttpResponse(text)

def items_all(request):
    text = ""
    for i in items:
        text = text + f'<br/><a href="/item/{i["id"]}">{i["id"]}</a>. Наименование: {i["name"]}, количество: {i["quantity"]}'
    return HttpResponse(text)