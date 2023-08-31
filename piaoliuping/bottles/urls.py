from django.urls import path
from .views import BottlePage, CreateBottlePage

app_name = 'bottles'

urlpatterns = [
    path('rand-bottle/', BottlePage.as_view(), name='random_bottle'),
    path('create-bottle/', CreateBottlePage.as_view(), name='create_bottle'),
]
