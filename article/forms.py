from django import forms
from .models import Article
class ArticleForm(forms.ModelForm) : 
    class Meta :                                                  #burada yaptığımız şey önceden article oluşturmuştuk dedik ki onu al getir ModelForm aracılığıyla                                                                            
        model = Article                                           #ve içine aynı modelin sadece fields fonk ile belirttik biz burada title ve content olmasını istiyoruz dedik
        fields = ["title","content","article_image"]

