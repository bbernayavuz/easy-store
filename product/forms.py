from django import forms

from product.models import Category, Product


class ProductForm(forms.ModelForm):

    # category = forms.ModelChoiceField(queryset=Category.objects.all().order_by("name"))

    class Meta:
        model = Product
        fields = "__all__"
