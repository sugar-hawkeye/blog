from django import forms

from .models import Article

from my_web.apps.mkeditor.widgets import MarkdownWidget

class ArticleForm(forms.ModelForm):
    # content = forms.CharField(widget=AdminPagedownWidget)
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': MarkdownWidget,
        }
