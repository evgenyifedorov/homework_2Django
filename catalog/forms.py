from django import forms

from catalog.models import Product, Version
from common.views import StyleFormMixin


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ("product_name", "description", "image", "price", "category")

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get("product_name")
        words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError("Недопустимое значение")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")
        words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError("Недопустимое значение")
        return cleaned_data


class ModeratorProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ("category", "description", "is_published")


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ("number_version", "name_version", "version_flag")
