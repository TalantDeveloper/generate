from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),

    path('links/', views.link_views, name='links'),
    path('links/create/', views.link_create, name='link_create'),
]
