from .views import checkout
from django.urls import path

urlpatterns = [
    path('payment/',checkout),
]
