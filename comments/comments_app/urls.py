from django.urls import path
from . import views

app_name = 'comments_app'

urlpatterns = [
    path('', views.main, name='main'),
    path('comment/', views.comment, name='comment')
]
