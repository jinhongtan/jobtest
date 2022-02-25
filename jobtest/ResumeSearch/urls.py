
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('index/search_job', views.search_job, name='search_job'),
    path('index/test_ajax', views.test_ajax),

]
