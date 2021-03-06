from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single/', views.single, name='single'),
    path('all/', views.get_all_record, name='get_all_record')
]