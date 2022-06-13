from django.urls import path, include
from .views import SimpleFormView

urlpatterns = [
    path('', SimpleFormView.as_view(), name='home'),
]