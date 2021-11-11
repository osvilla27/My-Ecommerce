from django.shortcuts import render

from product.models import Product


def index(request):
    products_latest = Product.objects.all().order_by('-id')[:3]
    context = {'products_latest': products_latest}
    return render(request, 'home/index.html', context)

