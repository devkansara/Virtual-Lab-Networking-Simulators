from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add2',views.add,name='add'),
    path('<slug:name>',views.base,name='base')
]