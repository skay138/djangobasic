from django.urls import path
from . import views

urlpatterns = [
    path('', views.apis_view),
    path('class', views.class_view.as_view())
]
