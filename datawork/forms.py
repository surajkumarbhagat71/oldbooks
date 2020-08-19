from django import forms
from .models import Category,Topic,Books

class BookInsert(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ('book_doc','book_status')