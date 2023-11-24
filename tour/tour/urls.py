from django.urls import path, re_path
from hello import views
 
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^about', views.about, name='about'),  ## r'^about' for finding if starts with 'about'
    re_path(r'^about/contact', views.contact, name='contact'),
    path('text', views.text, name='text'),
    path('introduce', views.introduce, name='introduce', kwargs={'name':'Izzat', 'age':20}),
]