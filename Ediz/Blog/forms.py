from django import forms
from .models  import BlogGonderi

class GonderiForm(forms.ModelForm):
    class Meta:
        model=BlogGonderi
        fields = ("baslik","yazi","eposta")
        labels = {"baslik":"Başlık","yazi":"İçerik","eposta":"E Posta"}