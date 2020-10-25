from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def FirstPage(req):
    return render(req, 'myweb/base.html')

def RegisterView(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(req, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(req, 'myweb/register.html', {'form': form})

def LogoutView(req):
    logout(req)
    return redirect("/")

@login_required
def Blog01(req):
    return render(req, 'myweb/blog01.html')
@login_required
def Blog02(req):
    return render(req, 'myweb/blog02.html')


#login


