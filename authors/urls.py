from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_authors, name='authors'),
    path('<int:author_id>/', views.author_detail, name='author_detail'),
]
