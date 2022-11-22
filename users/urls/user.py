from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views.users import UserListView, UserDetailView, \
    UserCreateView, UserDeleteView, UserUpdateView

urlpatterns = [
    path("", UserListView.as_view()),
    path("<int:pk>/", UserDetailView.as_view()),
    path("create/", UserCreateView.as_view()),
    path("<int:pk>/delete/", UserDeleteView.as_view()),
    path("<int:pk>/update/", UserUpdateView.as_view()),
    # auth
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
