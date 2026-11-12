from django import forms

from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('name', 'email', 'title', 'category', 'priority', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Как к вам обращаться'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@example.com'}),
            'title': forms.TextInput(attrs={'placeholder': 'Кратко опишите проблему'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Что произошло и какая помощь нужна?'}),
        }


