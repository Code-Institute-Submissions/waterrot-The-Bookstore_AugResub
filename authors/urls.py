from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_authors, name='authors'),
    path('<int:author_id>/', views.author_detail, name='author_detail'),
    path('add/', views.add_author, name='add_author'),
    path('edit/<int:author_id>/', views.edit_author, name='edit_author'),
    path('delete/<int:author_id>/', views.delete_author, name='delete_author'),
]
