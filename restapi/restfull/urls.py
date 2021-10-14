from rest_framework import routers

from django.urls import path, include
from rest_framework import routers
from  . import views

urlpatterns = [
    path('', views.hello_world),
    path('detail/<str:id>', views.detail),
    path('create/', views.create),
    path('update/<str:id>', views.update),
    path('delete/<str:id>', views.delete),

]
