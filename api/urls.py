from django.urls import path
from .views import RegisterView, PublicView, ProtectedView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('public/', PublicView.as_view(), name='public_api'),
    path('private/', ProtectedView.as_view(), name='private_api'),
]