from django.urls import path
from .views import FineView, Completed

urlpatterns = [
    path('', FineView.as_view(), name='home'),
    path('completed', Completed.as_view(), name='completed')
]