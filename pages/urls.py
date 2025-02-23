from django.urls import path
from .views import homepagepiew
urlpatterns = [
    path('', homepagepiew, name='home')
]