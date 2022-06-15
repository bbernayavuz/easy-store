from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer



<<<<<<< HEAD
def product_list(request):
    products = Product.objects.all()
    if products:
        return render(request, "product_list.html", {"products": products})

    else:
        return redirect("/create")


def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/list")
    return render(request, "product_create.html", {"form": form})


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
=======
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("name")
    serializer_class = ProductSerializer    
>>>>>>> 0925a05c98cb76ef4af3c1a3ba79d5917b0a2e22
