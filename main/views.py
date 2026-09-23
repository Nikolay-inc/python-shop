from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    print(products)
    print(categories)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'main/product/list.html', {'products': products, 'categories': categories, 'category': category})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)[:4]

    return render(request, 'main/product/detail.html', {'product': product, 'related_products': related_products})

# def category_list(request):
#     categories = Category.objects.all()
#     return render(request, 'main/category/list.html', {'categories': categories})

# def category_detail(request, id):
#     category = get_object_or_404(Category, id=id)
#     return render(request, 'main/category/detail.html', {'category': category})
