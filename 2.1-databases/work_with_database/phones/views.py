from django.shortcuts import render, redirect
from phones.models import Phone



def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort_product = request.GET.get('sort')
    phones_objects = Phone.objects.all().reverse()

    sort_mapping = {
        "max_price": "price",
        "min_price": "-price",
        "name": "name"} 
    
    if sort_product:
        new_sort = request.GET.get('sort')
    else:
        new_sort = 'name'
    phones_objects = phones_objects.order_by(sort_mapping.get(new_sort))
    context = {'phones': phones_objects}
    return render(request, template, context=context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context=context)