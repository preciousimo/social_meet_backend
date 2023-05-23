from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('me/', views.me, name='me'),
    path('signup/', views.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('friends/<uuid:pk>/', views.friends, name='friends'),
    path('friends/<uuid:pk>/request/', views.send_friendship_request, name='send_friendship_request'),
    path('friends/<uuid:pk>/<str:status>/', views.handle_request, name='handle_request'),
]