from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
# Create your views here.
text_all = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

text_all2 = """
    Имя: <strong>Иван</strong> <br/>
    Отчество: <strong>Петрович</strong><br/>
    Фамилия: <strong>Иванов</strong><br/>
    телефон: <strong>8-923-600-01-02</strong><br/>
    email: <strong>vasya@mail.ru</strong>
    """
"""items = [   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
            {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
            {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
            {"id": 7, "name": "Картофель фри" ,"quantity":0},
            {"id": 8, "name": "Кепка" ,"quantity":124},]"""

def home_old(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Носик Л.С.</i>
    """
    return HttpResponse(text)

def home(request):
    context = {
        "name": "petrov ivan",
        "email": "asd@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    context = text_all
    return render(request, "about.html", context)

def get_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        colors = item.colors.all()
        context = {"item": item, 'colors': colors,}
    except:
        context = {"error": f'Товар с id = {item_id } не найден'}
        return render(request, 'error_page.html', context)
    return render(request, 'item.html', context)

def get_items(request):
    qs = Item.objects.all()
    context = {"items": qs}
    return render(request, "items.html", context)