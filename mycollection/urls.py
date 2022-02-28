from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search',views.search, name = 'search'),
    re_path(r'^location/(?P<location>\w+)/', views.image_location, name='location'),

]