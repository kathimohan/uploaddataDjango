
from django.urls import path
from . views import *
urlpatterns = [
    path('', json_api.as_view()),
]
