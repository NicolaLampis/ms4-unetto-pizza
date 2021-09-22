from django import forms
from .models import Product, Category, Allergen, Deal


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_friendly_names = [
            (category.id, category.get_friendly_name())
            for category in categories
        ]

        allergens = Allergen.objects.all()
        allergen_friendly_names = [
            (allergen.id, allergen.get_friendly_name())
            for allergen in allergens
        ]

        deals = Deal.objects.all()
        deal_friendly_names = [
            (deal.id, deal.get_friendly_name())
            for deal in deals
        ]

        self.fields['category'].choices = category_friendly_names
        self.fields['allergen'].choices = allergen_friendly_names
        self.fields['deal'].choices = deal_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'allauth-form-inner-content form-group'
