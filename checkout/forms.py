from django import forms
from .models import Order

CITIES = [
    ('', 'Select a City *'),
    ('Amsterdam', 'Amsterdam'),
    ('Utrecht', 'Utrecht')
]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email',
                  'telephone', 'address_line1',
                  'address_line2', 'town_or_city',
                  'postcode')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, add * to required fields,
        set autofocus on first field and remove labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'telephone': 'Phone Number',
            'address_line1': 'Street Address 1',
            'address_line2': 'Street Address 2',
            'postcode': 'Postal Code',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        self.fields['town_or_city'] = forms.ChoiceField(choices=CITIES)
        for field in self.fields:
            if field != 'town_or_city':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields['town_or_city'].widget.attrs['class'] = 'form-select stripe-style-input'
            self.fields[field].label = False
