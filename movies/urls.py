from django.urls import path
from .views import ListCreateMoviesView, RetrieveUpdateDestroyMoviesView, ListCreateReviewView, ListCreateCommentView

urlpatterns = [
    path('movies/', ListCreateMoviesView.as_view()),
    path('movies/<int:pk>/', RetrieveUpdateDestroyMoviesView.as_view()),
    path('movies/<int:pk>/review/', ListCreateReviewView.as_view()),
    path('movies/<int:pk>/comments/', ListCreateCommentView.as_view())
]
