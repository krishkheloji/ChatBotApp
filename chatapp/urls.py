from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('chat',views.Chat.as_view(),name="chat"),
    path('login',views.Login.as_view(),name="login"),
    path('logout',views.logout,name="logout"),
]