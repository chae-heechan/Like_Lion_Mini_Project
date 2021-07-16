from shoppingmall.models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib import auth

from .models import User

def home(request):
    products = Product.objects.all()  
    paginator = Paginator(products, 3)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    return render(request, 'home.html', {'page':page})

def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'detail.html', {'product':product})

def user_signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            new_user = User()
            new_user.user_name = request.POST["user_name"],
            new_user.user_id = request.POST["user_id"],
            new_user.user_password = request.POST["password"],
            new_user.user_university = request.POST["user_university"],
            new_user.save()
            auth.login(request, new_user)
            return redirect('home')

        else:
            return render(request, 'signup.html')
    
    else:
        return render(request, 'signup.html')

def user_login(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        user_password = request.POST["user_password"]

        user = authenticate(username = user_id, password = user_password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'login.html', {'error': '아이디와 비밀번호가 맞지 않습니다.'})

    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')