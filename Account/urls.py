from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, GetProfile
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', GetProfile.as_view(), name='get_profile')
]