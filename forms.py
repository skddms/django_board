from django import forms
from django.forms import ModelForm
from .models import Board
from datetimepicker.widgets import DateTimePicker

class DateInput(forms.DateInput):
    input_type = 'date'

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'
        widgets = {
            'createDate': DateInput()
        }
