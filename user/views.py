from django.shortcuts import render , redirect
from .forms import RegisterForm , LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout                  #oturum açmak için #authenticate ise böyle bir kullanıcı var mı yok mu kontrol ediyor
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


    
# Create your views here.
#@csrf_exempt 
def register(request) : 
    
   #2. Yol daha kolay
    form = RegisterForm(request.POST or None)                 #register form post ise veya none ise demek o da none içi boş yanı get request oluyor
    if form.is_valid():                                     #burda gider clean methodunu çağırır clean methodu ise passwordları kıyaslıyordu aynı mı diye ve post requesse buraya girer
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla kayıt oldunuz...")
        return redirect("index")
    
    context = {
        "form" : form 
    }
    return render(request,"register.html",context)
    

    #1.Yol
    """if request.method == "POST" :
        form = RegisterForm(request.POST)
        if form.is_valid():                                              #burda gider clean methodunu çağırır clean methodu ise passwordları kıyaslıyordu aynı mı diye
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,"Başarıyla kayıt oldunuz...")
            return redirect("index")

        context = {
            "form" : form 
        }
        return render(request,"register.html",context)
        
    else : 
        form = RegisterForm()
        context = {
            "form" : form 
        }
        return render(request , "register.html" , context)"""


#Giriş Yap
@csrf_exempt 
def loginUser(request) :
    form = LoginForm(request.POST or None) 
    context = {
        "form" : form
    }
   
    if form.is_valid() :
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username,password = password)
        if user is None :                   #böyle bir kullanıcı yoksa komtrolü
            messages.warning(request , "Kullanıcı adı veya parola yanlış")
            return render(request , "login.html",context)
        
        messages.success(request,"Başarıyla giriş yaptınız...")
        login(request,user)
        return redirect("index")
    
    return render(request,"login.html",context)

def logoutUser(request) :
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı...")
    return redirect("index")