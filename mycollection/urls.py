from django.urls import path, re_path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('search',views.search, name = 'search'),
    re_path(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)