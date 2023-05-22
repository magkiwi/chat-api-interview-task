from django.urls import re_path, include
from chat.views.conversation import ConversationViewSet
from rest_framework.routers import DefaultRouter
from . import sockets

default_router = DefaultRouter()

api_urls = []
default_router.register(r"conversations", ConversationViewSet, basename="conversation")

api_urls += default_router.urls

urlpatterns = [
    re_path('', include(api_urls)),
]

websocket_urlpatterns = [
    re_path(r'', sockets.ChatConsumer.as_asgi())
]
