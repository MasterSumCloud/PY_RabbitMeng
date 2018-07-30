"""RabbitMeng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path

from account import views as User
from blacklist import views as Black
from tumengclans import views as TumengClans

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regist', User.regist),
    path('login', User.login),
    path('changepass', User.changepass),
    path('currentwar', User.currentwar),
    path('clans', User.clans),
    path('players', User.players),
    path('addblaclk', Black.addblaclk),
    path('deletebalck', Black.deletebalck),
    path('getblack', Black.getblack),
    path('gettumengclans', TumengClans.gettumengclans),

    # path(r'^logout/$', views.logout),
]

