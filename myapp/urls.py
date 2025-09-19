from django.urls import path
from . import views

urlpatterns = [
    path('',views.userreg,name="userreg"),
    path('ins/',views.insertuser,name="ins"),
    path('',views.index,name="index"),
    path('users/',views.viewuser,name="viewuser"),
    path("del/<str:id>",views.deleteuser,name='deleteuser'),
    path("edit/<int:uid>/",views.update_user,name='update_user'),
    path("home/",views.home_page,name="homepage"),
]