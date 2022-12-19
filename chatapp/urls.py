from django.urls import path
from .views import *

urlpatterns = [
    path("chat/", ChatLogDetail.as_view()),
    path('home', home_page, name="home")
]