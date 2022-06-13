from math import prod

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from product.forms import ProductForm
from product.models import *


def product_list(request):
    products = Product.objects.all()
    if products:
        return render(request, "product_list.html", {"products": products})

    else:
        return redirect("/list")


def product_create(request):
    form = ProductForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        form.save()
        return redirect("/list")

    return render(request, "product_create.html", context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product_update.html", {"product": product})


def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        product = form.save(commit=False)
        product.save()
        messages.success(request, "Ürün başarıyla güncellendi")
        return redirect("/list")
    return render(request, "product_update.html", {"form": form})


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, "Ürün başarıyla silindi")
    return redirect("/list")
