from django.urls import path
from .views import DisplayBase

urlpatterns = [
    
    path('', DisplayBase.as_view(), name='base')
]