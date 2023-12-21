from django.shortcuts import render
from products.models import *

def products_page_view(request):
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    company = request.GET.get('company')
    tag = request.GET.get('tag')
    color = request.GET.get('color')
    page = request.GET.get('page')
    sort = request.GET.get('sort')
    products = ProductModel.objects.all().order_by('-pk')
    if page:
        page = int(page) - 1
        products = products[page * 1: page * 1 + 1]
    if q:
        products = products.filter(title__icontains=q)
    if cat:
        products = products.filter(categories=cat)
    if company:
        products = products.filter(companies=company)
    if tag:
        products = products.filter(tags=tag)
    if color:
        products = products.filter(colors=color)
    if sort:
        if sort == "-price":
            products = products.order_by('-price')
        elif sort == "price":
            products = products.order_by('price')

    categories = CategoryModel.objects.all()
    companies = CompanyModel.objects.all()
    tags = TagModel.objects.all()
    colors = ColorModel.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "companies": companies,
        "tags": tags,
        "colors": colors,
        "page_total": range(1, len(products) + 1)
    }
    return render(request, 'product-list.html', context)
