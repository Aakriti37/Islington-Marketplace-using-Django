from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:id>/', views.blog_detail, name='blog_detail')
]