from django.shortcuts import render, redirect
#from django.http import HttpResponse
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    tipe_sort = request.GET.get("sort", 'name')
    if tipe_sort == 'min_price':
        phones = Phone.objects.order_by('price')
        template = 'catalog.html'
        context = {
            'phones': phones,
        }
    else:
        phones = Phone.objects.order_by('nаme')
        template = 'catalog.html'
        context = {
            'phones': phones,
        }

    return render(request, template, context=context)


def show_product(request, slug):
    phone = Phone.objects.get(slug == slug)
    template = 'product.html'
    context = {
        'phone': phone,
    }
    return render(request, template, context=context)
