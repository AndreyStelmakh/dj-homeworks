from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    else:
        if sort == 'min_price':
            phone_objects = Phone.objects.all().order_by('price')
        else:
            if sort == 'max_price':
                phone_objects = Phone.objects.all().order_by('-price')

    phones = [phone for phone in phone_objects]
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug=slug)
    phones = [phone for phone in phone_objects]
    context = {'phone': phones[0]}
    return render(request, template, context)
