from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter the expense',
                'class': 'form-control',
            }),
            'amount': forms.NumberInput(attrs={
                'placeholder': 'Enter the amount',
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
        }