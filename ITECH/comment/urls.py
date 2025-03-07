
from django.urls import path
from comment import views
app_name = 'comment'
urlpatterns = [
    path('comment_post/<int:restaurant_id>/',  views.comment_post, name='comment_post'),
]