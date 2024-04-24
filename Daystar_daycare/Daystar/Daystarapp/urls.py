from django.urls import path
from Daystarapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminreg/', views.addadmins, name='addadmins'),
    path('adminlog/', views.adminlogin, name='adminlogin'),
    path('babiesreg/', views.addbabies, name='addbabies'),
    path('sittersreg/', views.addsitter, name='addsitter'),
]