from django.urls import path

from . import views

urlpatterns = [
    path('ipv4addressing/',views.mainpage,name='mainpage'),
    path('',views.firstpage,name='firstpage'),
    path('ipv4addressing/sim/',views.sim,name='sim'),
    path('simpleparitycheck/',views.experiment2,name='simpleparitycheck'),
    path('simpleparitycheck/sim/',views.simpleparitycheck,name='simpleparitychecksim')
]