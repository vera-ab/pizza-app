from django import forms

from .models import Order, Pizza


class CustomPizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['title', 'ingredients']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_title(self):
        return f'{self.cleaned_data["title"]} (custom)'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone_number', 'name', 'comments']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        return f'{self.cleaned_data["name"]}'
