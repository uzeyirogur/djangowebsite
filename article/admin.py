from django.contrib import admin
from .models import Article                                 #Admin panelinde göstermek için bu işlemi yaptık    

# Register your models here.

@admin.register(Article)                                      #panelde gösterdik ve kayıt etmek için şart
class ArticleAdmin(admin.ModelAdmin) :
    list_display = ["title","author","created_date"]          #admin panelinde göstermek istediğimiz kısımlar için
    list_display_links = ["title","created_date"]             #yazdığımız şeylere link atıyor tarihe bastığımızda da makaleye giriyor
    search_fields = ["title"]                                 #title bilgisine göre search kısmı çıkartır
    list_filter = ["created_date"]                             #son 7 gün son bir ay vs filtreleme yapmak için
    class Meta : 
        model = Article   