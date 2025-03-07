from django.urls import path
from django.conf.urls import include
from userprofile import views
app_name = 'userprofile'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),  # 注册视图
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('register_restaurant/', views.register_restaurant, name='register_restaurant'),
    path('restaurant_delete/<int:id>/', views.restaurant_delete, name='restaurant_delete'),
    path('restaurant_update/<int:id>/', views.restaurant_update, name='restaurant_update'),
]