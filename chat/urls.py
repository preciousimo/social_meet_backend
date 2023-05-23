from django.urls import path

from . import views


urlpatterns = [
    path('', views.conversation_list, name='conversation_list'),
    path('<uuid:pk>/', views.conversation_detail, name='conversation_detail'),
    path('<uuid:pk>/send/', views.conversation_send_message, name='conversation_send_message'),
    path('<uuid:user_pk>/get-or-create/', views.conversation_get_or_create, name='conversation_get_or_create'),
]