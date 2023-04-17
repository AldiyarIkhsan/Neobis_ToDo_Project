from django import forms
from todolist.models import ToDo

class ToDoForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = (
            "title",
            "description",
        )

class OrderForm(forms.Form):
    order_by = forms.ChoiceField(choices=[
        ('created_date', 'created_date'),
        ('-created_date', '-created_date'),
    ])
