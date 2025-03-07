from django.urls import path
from IT import views

app_name = 'IT'

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('restaurant_detail/<int:id>/',  views.restaurant_detail, name='restaurant_detail'),
    path('introduction/',  views.introduction, name='introduction'),
]