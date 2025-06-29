from django.urls import path
from .views import notif_list

urlpatterns = [
    path('notifications/', notif_list, name='notifications'),
]
