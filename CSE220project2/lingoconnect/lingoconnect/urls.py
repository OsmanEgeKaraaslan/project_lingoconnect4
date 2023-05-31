"""lingoconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from polls import views
from django.contrib.auth import views as auth_views

app_name = 'polls'

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('question/', views.question, name='question'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='polls:home'), name='logout'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
    path('accounts/', include('django.contrib.auth.urls'),{'template_name': 'login.html'}),
    path('custom-login/', views.custom_login_view, name='custom_login'),

]
