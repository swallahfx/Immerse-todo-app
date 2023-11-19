from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profiles/', UserProfileListCreateView.as_view(), name='user_profile_list_create'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDestroyView.as_view(), name='user_profile_retrieve_update_destroy'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
