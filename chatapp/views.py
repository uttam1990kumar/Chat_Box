from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .consumers import ChatConsumer

# Create your views here.
class ChatLogDetail(APIView):
    def post(self, request):
        messages=request.data['message']
        channel_layer = get_channel_layer()   
    
        async_to_sync(channel_layer.group_send)(
            "room_name", {
                "type": "chat_message", 
                "message": messages
                }
        )
        
        return Response(messages)
    
    
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def home_page(request):
    subject, from_email, to = 'hello', 'zuhoo123@zohomail.in', 'uttam3392kumar@gmail.com'
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message From Uttam.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse("Success Bro..")
    