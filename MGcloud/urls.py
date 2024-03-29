"""MGcloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from django.contrib import admin
from baton.autodiscover import admin
from django.urls import path, include

from Auth import views as atv
from Cloud import views as ctv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),

    path('Home/', atv.Home),
    path('SignUp/', atv.Register),
    path('SignIn/', atv.SignIn),
    path('logout/', atv.logoutuser),

    path('', ctv.Home),
    path('Files/', ctv.Files),
    path('About/', ctv.About),
    path('Download/<str:pk_download>/', ctv.Download, name='Download'),
    path('Delete/<str:pk_delete>/', ctv.Delete, name='Delete'),
    path('Open/<str:pk_open>/', ctv.Open, name='Open'),
]
