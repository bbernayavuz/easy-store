from django import forms

from product.models import Category, Product


class ProductForm(forms.ModelForm):

    # category = forms.ModelChoiceField(queryset=Category.objects.all().order_by("name"))

    class Meta:
        model = Product
<<<<<<< HEAD
        fields = "__all__"
=======
        exclude = ('slug',)
>>>>>>> 0925a05c98cb76ef4af3c1a3ba79d5917b0a2e22
