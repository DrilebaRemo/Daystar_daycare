from django.urls import path
from Daystarapp import views
from Daystarapp import views as auth_views
#from django.contrib.auth import logout

urlpatterns = [
    path('', views.index, name='index'),
    path('adminreg/', views.addadmins, name='addadmins'),
    path('adminlog/', views.adminlogin, name='adminlogin'),
    path('logoutuser/', auth_views.logoutuser, name='logout'),
    path('babiesreg/', views.addbabies, name='addbabies'),
    path('sittersreg/', views.addsitter, name='addsitter'),
    path('home/', views.homes, name='homes'),
    path('about/', views.about, name='about'),
    path('babystatus/', views.babyview, name='babyview'),
    path('sitterstatus/', views.sitterview, name='sitterview'),
    path('assign/', views.assignbabyview, name='assignbabyview'),
    path('assignrecord/', views.assignrec, name='assignrec'),
    path('babypick/', views.pickbaby, name='pickbaby'),
    path('pickrec/', views.babypickview, name='babypickview'),
    path('editsitterview/<int:id>/', views.editsitterview, name='editsitterview'),
    path('deletesitterview/<int:id>/', views.deletesitterview, name='deletesitterview'),
    path('editbabyview/<int:id>/', views.editbabyview, name='editbabyview'),
    path('deletebabyview/<int:id>/', views.deletebabyview, name='deletebabyview'),
    path('sales/', views.sales_view, name='sales_view'),
    path('salerecord/', views.salerecord, name='salerecord'),
    path('dollreg/', views.regdoll, name='regdoll'),
    path('procure/', views.procure_view, name='procure_view'),
    path('procuregive/', views.procuregive, name='procuregive'),
    path('procurerec/', views.procure_record, name='procure_record'),
    path('prooverall/', views.prototalview, name='prototalview'),
    path('dolloverall/', views.dolltotalview, name='dolltotalview'),
    path('editdollview/<int:id>/', views.editdollview, name='editdollview'),
    path('deletedollview/<int:id>/', views.deletedollview, name='deletedollview'),
    path('editproview/<int:id>/', views.editproview, name='editproview'),
    path('deleteproview/<int:id>/', views.deleteproview, name='deleteproview'),
    path('deletesaleview/<int:id>/', views.deletesaleview, name='deletesaleview'),
]