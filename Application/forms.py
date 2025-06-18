from django import forms
from .models import House

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HouseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
