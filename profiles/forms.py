from django import forms
from .models import UserProfile

CITIES = [
    ('', 'Select a City'),
    ('Amsterdam', 'Amsterdam'),
    ('Utrecht', 'Utrecht')
]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, set autofocus on first field and remove labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_telephone': 'Phone Number',
            'default_address_line1': 'Address Line 1',
            'default_address_line2': 'Address Line 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postal Code',
        }

        self.fields['default_telephone'].widget.attrs['autofocus'] = True
        self.fields['default_town_or_city'] = forms.ChoiceField(choices=CITIES)
        for field in self.fields:
            if field != 'default_town_or_city':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields['default_town_or_city'].widget.attrs['class'] = 'profile-form-input form-select'
            self.fields[field].label = False
