from django.http import HttpResponse
from django.shortcuts import render

from phones.models import Phone


# Create your views here.
def index(request):
    template = 'index.html'
    context = {}
    return render(request, template, context=context)
def show_catalog(request):
    template = 'catalog.html'
    # читаем параметр в запросе
    sort_pages = request.GET.get('sort')
    phones = Phone.objects.all()
    # сортировка
    if sort_pages == 'max_price':
        phones = phones.order_by('price').reverse()
    elif sort_pages == 'min_price':
        phones = phones.order_by('price')
    elif sort_pages == 'name':
        phones = phones.order_by('name')
    # передаем контент в шаблон
    context = {
                'phones': phones,
              }
    # рисуем страницу
    return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    # поиск по slug
    phone = Phone.objects.get(slug=slug)
    # передаем контент в шаблон
    context = {
                'phone': phone
              }
    # рисуем страницу
    return render(request, template, context=context)