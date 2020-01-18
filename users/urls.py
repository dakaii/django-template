from django.urls import path

from .views import LoginView, SignUpView, UserDetail, UserList

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='users-detail'),
]
