from django.shortcuts import render, redirect
#from django.http import HttpResponse
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    phone_objects = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phone.name': [f'{n.name}' for n in phone_objects],
        'phone.prise': [f'{p.prise}' for p in phone_objects],
        'phone.image': [f'{i.image}' for i in phone_objects],
        'phone.slug': [f'{s.slug}' for s in phone_objects],
    }
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.get(slug == slug)
    template = 'product.html'
    context = {
        'phone.name': f'{phone_object["name"]}',
        'phone.prise': f'{phone_object["prise"]}',
        'phone.image': f'{phone_object["image"]}',
        'phone.release_date': f'{phone_object["release_date"]}',
        'phone.lte_exists': f'{phone_object["lte_exists"]}',
    }
    return render(request, template, context)
