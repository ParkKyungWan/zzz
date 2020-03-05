"""zzz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import zzz_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',zzz_app.views.home,name='home'),
    path('sleep/',zzz_app.views.sleep,name='sleep_time'),
    path('wake/',zzz_app.views.wake,name='wakeup_time'),
    path('zzz/',zzz_app.views.now,name='now'),
    path('wakeup/',zzz_app.views.wakeup,name='not_now'),
]
