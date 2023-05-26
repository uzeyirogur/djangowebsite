from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .forms import Article
# Create your views here.
def index(request) :  
    #return HttpResponse("Anasayfa")           #iki yolla yapabiliriz
    
    return render(request,"index.html")

def about(request) :
    return render(request,"about.html")

def dashboard(request)  :
    articles = Article.objects.filter(author = request.user)                         #sisteme şuan kim girmişse onun articlelarını getir demek
    context = {
        "articles" : articles
    }
    return render(request,"dashboard.html",context) 

def addarticle(request) :
    form = ArticleForm(request.POST or None)

    if form.is_valid() :
        article = form.save(commit = False)         #sen oluştur ama kaydetme dedik
        article.author = request.user               #article yazarını aldık usera atadık
        article.save()                               #en son kayıt 
        messages.success(request,"Makaleniz başarıyla oluşturuldu...")
        return redirect("index")

    return render(request,"addarticle.html",{"form" : form})
    
def detail(request,id) :
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)            #vars üstteki gibi gelcek yoksa 404 hata atıcak
    return render(request,"detail.html",{"article" : article})