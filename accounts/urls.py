from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, LoginView

urlpatterns = [
    path('accounts/', UserListCreateView.as_view()),
    path('accounts/<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),
    path('login/', LoginView.as_view()),
    path('login/', LoginView.as_view()),

]
