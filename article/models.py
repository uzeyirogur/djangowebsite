from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model) :
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)   #Yazarı kullanıcıdan al ve bu kullanıcı silinirse onun hakkında her şeyi de sil demek
    title = models.CharField(max_length = 50 , verbose_name = "TİTLE")                            #başlığı oluşturduk ve max 50 olsun 
    content =   RichTextField(verbose_name = "İÇERİK")                  #verbose_name biz isim vermek istiyoruz demek
    created_date = models.DateTimeField(auto_now_add = True)             #Oluşturulma zamanını tanımladık ve biz buraya tarih vermicez ne zaman oluşmuşsa o zamanı otomatik alıcak
   
    def __str__(self) :
        return self.title                                                #Ekranda normalde articles 1 diye gözüküyordu bunu yaptığımızda artık ana ekranda kendi title ile gözükecek
    article_image = models.FileField(blank = True , null = True, verbose_name = "Makaleye fotoğraf ekleyin")