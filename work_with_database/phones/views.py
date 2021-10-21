from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    param = request.GET.get('sort')
    if param == 'name':
        query = Phone.objects.order_by('name')
    elif param == 'min_price':
        query = Phone.objects.order_by('price')
    elif param == 'max_price':
        query = Phone.objects.order_by('-price')
    else:
        query = Phone.objects.all()
    context = {'phones': query}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    query = Phone.objects.get(slug=slug)
    context = {'phone': query}
    return render(request, template, context)
