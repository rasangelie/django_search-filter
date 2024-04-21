from django.urls import path
from .import views

urlpatterns = [
    path('search/', views.UserListView.as_view(), name='search')
]
