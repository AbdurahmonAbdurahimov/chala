
from django.urls import re_path
from websocket.consumers import InventoryConsumer

websocket_urlpatterns = [
    re_path(r'ws/inventory/$', InventoryConsumer.as_asgi()),
]
