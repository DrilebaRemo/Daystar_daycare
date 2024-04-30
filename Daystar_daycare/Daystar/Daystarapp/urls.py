from django.urls import path
from Daystarapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminreg/', views.addadmins, name='addadmins'),
    path('adminlog/', views.adminlogin, name='adminlogin'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('babiesreg/', views.addbabies, name='addbabies'),
    path('sittersreg/', views.addsitter, name='addsitter'),
    path('home/', views.homes, name='homes'),
    path('about/', views.about, name='about'),
    path('babystatus/', views.babyview, name='babyview'),
    path('sitterstatus/', views.sitterview, name='sitterview'),
    path('pay/', views.payfor, name='payfor'),
    path('dropbaby/', views.babydrop, name='babydrop'),
    path('babypick/', views.pickbaby, name='pickbaby'),
]