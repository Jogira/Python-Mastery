from django.urls import path
from . import views
#movies
urlpatterns = [
    path('', views.index, name='index')
]