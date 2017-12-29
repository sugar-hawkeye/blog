from django import forms

from pagedown.widgets import AdminPagedownWidget
from .models import Article

class ArticleForm(forms.ModelForm):
    # content = forms.CharField(widget=AdminPagedownWidget)
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': AdminPagedownWidget,
        }