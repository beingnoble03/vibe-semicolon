from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registerpage/', views.register_page, name= "register-page"),
    path('loginpage/', views.login_page, name = "login-page"),
    path('logout/', views.logout_my, name = "logout-user"),
    path('register/', views.register_my, name = "register-user"),
    path('login/', views.login_my , name="authenticate-user"),
    path('profile/', views.profile_page , name="profile-page"), 
    path('profileuser/<str:username>/', views.profile_page_other, name = "profile-page-other"),
    path('updateprofile/', views.update_profile, name = "update-profile"),
    path('feed/', views.feed, name= "feed"),
    path('matchyes/', views.match_yes, name = "match-yes"),
    path('pictureupload/', views.picture_upload, name = "picture-upload"),
]
