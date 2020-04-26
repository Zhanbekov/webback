from django.urls import path
from api import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path('articles/', views.articles),
    path('articles/publish/', views.articles_for_publisher),
    
]