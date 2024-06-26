"""
URL configuration for Resume_Extractor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    # path('',views.base,name='base'),
    path('admin/', admin.site.urls),
    # path('upload/',views.upload_file,name='upload'),
    # path('upload/',views.upload_file,name='upload_file'),
    path('',views.extraction_to_text,name="upload_file"),
    path('save_text_file/',views.save_to_text,name="s_text"),


]