from django.urls import path
from .views import BottlePage

app_name = 'bottles'

urlpatterns = [
    path('rand-bottle/', BottlePage.as_view(), name='random_bottle'),
]
