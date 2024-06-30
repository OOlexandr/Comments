from django.urls import path
from . import views

app_name = 'comments_app'

urlpatterns = [
    path('', views.view_comment, name='view_comments'),
    path('comment/', views.add_comment, name='add_comment'),
    path('reply/', views.add_reply, name='add_reply'),
    path('edit/', views.edit_comment, name='edit_comment')
]
