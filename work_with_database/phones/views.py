from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {
        'phone.name': ,
        'phone.price',
        'phone.image',
        'phone.slug',

    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
