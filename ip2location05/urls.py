"""ip2location05 URL Configuration

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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

from ip2location05app.views.PublicView import PublicView
from ip2location05app.views.SingleIPHistoryView import SingleIPHistoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('ip2location05app.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('', PublicView.as_view())
]
