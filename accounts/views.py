from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
import requests
from django.http import HttpResponse
from django.http import Http404
from accounts.models import ShortUrls
@login_required
def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser==False or User.is_anonymous==False and request.user.is_superuser==False:
        if not Token.objects.filter(user_id = request.user.id).exists():
            token = Token.objects.create(user_id=request.user.id)
        context={
            'userid':request.user.id,
      }
        return render(request,'homepage/index.html',{'context':context})
    return render(request,'homepage/index.html')


def homepage(request):
    if not request.user.id:
        data = 3
        user = None
    else:
        data = request.user.id
        user = request.user
    context={
        'userid':data
    }
    if request.method=='POST':
        request.session.flush()
        url =request.POST['url']
        shorturl = hash(url)
        ShortUrls(user_id=user,url=url,ShortUrl=shorturl).save()
        request.session['shorturl']=f"{request.get_host()}/{shorturl}"
        return redirect('home')
    return render(request,'homepage/index.html',{'context':context})


def redirecting(request,path):
    print(path)
    t = ShortUrls.objects.filter(ShortUrl=path)
    if t.exists():
        redirectingurl = ShortUrls.objects.get(ShortUrl=path).url
        print(redirectingurl)
        return redirect(redirectingurl)
    else:
        return redirect('doesnotexist')

def doesnotexist(request):
    if not request.user.id:
        data = 3
    else:
        data = request.user.id
    context={'userid':data}
    return render(request,'errorpage/404.html',{'context':context})
