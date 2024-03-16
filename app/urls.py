
from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud, name="crud"),
    path('edit/<int:user_id>', views.edit, name="edit"),
    path('add/', views.add, name="add"),
    path('delete/<str:user_id>', views.delete, name="delete"),
]
