import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from chatapp.consumers import *


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbox.settings')

django_asgi_app = get_asgi_application()



# ws_patterns = [
#     path('chat/<str:room_code>', ChatConsumer.as_asgi())
    
# ]

# application = ProtocolTypeRouter({
#      "http": django_asgi_app,
#     "websocket": URLRouter(ws_patterns)
    
# })

application = ProtocolTypeRouter({
     "http": django_asgi_app,
     
    "websocket": URLRouter([
        path('chat/', ChatConsumer.as_asgi())
        
    ])
    
})