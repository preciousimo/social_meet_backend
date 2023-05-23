from django.urls import path

from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<uuid:pk>/like/', views.post_like, name='post_like'),
    path('profile/<uuid:id>/', views.post_list_profile, name='post_list_profile'),
    path('create/', views.post_create, name='post_create'),
]