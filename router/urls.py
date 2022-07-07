from django.urls import path

from .views import RegisterView, PresenceView, UnregisterView, MessageView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('presence', PresenceView.as_view(), name='presence'),
    path('unregister', UnregisterView.as_view(), name='unregister'),
    path('message', MessageView.as_view(), name='message'),
]
