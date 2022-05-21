"""blogproject URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    #html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    #django form을 이용한 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    #django modelform을 이용한 블로그 객체
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    path('detail/<int:blog_id>', views.detail, name='detail')
] 

#media 파일에 접근 가능한 url 추가해야함
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


