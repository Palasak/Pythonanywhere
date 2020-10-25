from django.contrib import admin
from django.urls import path
from myweb import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FirstPage, name='home'),
    path('Login/', auth_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
    path('Logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView),
    path('blog01/', views.Blog01),
    path('blog02/', views.Blog02),
]
