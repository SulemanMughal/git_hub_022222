from core import consumers
from django.urls import re_path
from django.conf.urls import url


websocket_urlpatterns = [
    url(r'^ws$', consumers.ChatConsumer.as_asgi()),
    # from . import consumers

    # websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
# ]
]

