from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.
from .models import *
from .serializers import *
class json_api(APIView):
    def get(self, request):
        data = jsondata.objects.all()
        serializer = jsonSerializer(data, many=True)
        return Response(serializer.data)
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        mnf=user.first_name
        userSerilizer = UserSerializer(user, many=False)
        #userSerilizer.data
        return Response({'token': token.key, 'mn':mnf })
