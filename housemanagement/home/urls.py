from django.urls import path
from .import views


urlpatterns = [
    path('', views.home_request, name='home'),
    path('', views.house_list, name='house_list'),
    path('<int:id>/<slug:slug>/', views.house_detail,name='house_detail'),
    path('login', views.login_request, name='login_request'),
    path('register', views.register_request, name='register'),
    path("logout", views.logout_request, name= "logout"),
]
