from django.urls import path
from .views import conv_list, conv_detail

urlpatterns = [
    path('conversations/', conv_list, name='conv_list'),
    path('conversations/<int:conv_id>/', conv_detail, name='conv_detail'),
]

urlpatterns = [
    # List all conversations
    path('conversations/', conv_list, name='conv_list'),

    # View an existing conversation
    path('conversations/<int:conv_id>/', conv_detail, name='conv_detail'),

    # Start or view a conversation with a specific user
    path('conversations/with/<str:other_username>/', conv_detail, name='conv_with'),
]