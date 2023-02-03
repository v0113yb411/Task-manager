from django.urls import path, include
from .import views

urlpatterns = [
    path("practice/", views.practice, name='practice'),
    path("demo/", views.index_demoapp, name='practice'),
]
