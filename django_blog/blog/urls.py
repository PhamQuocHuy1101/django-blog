from django.urls import path, include
from blog import views

urlpatterns  = [
    path("ip/", views.get_ip),
    path('', views.index),
    path('post/test', views.test),
    path('post/<slug>', views.post_detail, name='blog-post-detail'),
    
]