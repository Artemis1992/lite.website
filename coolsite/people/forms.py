from django import forms
from django.core.exceptions import ValidationError
from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
    class Meta:
        model = People
        # fields = "__all__"
        fields = ["title", "slug", "content", "photo", "is_published", "cat"] # Перечисляем какие поля мы будем использовать
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 400px;'}),
            "content": forms.Textarea(attrs={'cols': 60, 'rows': 10, 'style': 'width: 400px;'}),
            "slug": forms.TextInput(attrs={'class': 'form_input', 'style': 'width: 400px;'}),
        }
    
    def clean_title(self):
        title = self.cleaned_data['title'] # Получаем значение заголовка
        if len(title) > 200: # Проверяем длину заголовка
            raise ValidationError('Длина превышает 200 символов') # Генерируем ошибку валидации
        return title # Возвращаем значение, если оно корректное
    
    