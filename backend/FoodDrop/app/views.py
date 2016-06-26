from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

def index(request):

    data = {'test': 'response'}

    return JsonResponse(data)

@api_view(['POST'])
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponse("api-token-auth/")
    else:
        return HttpResponse("fail")

@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.data['email'], # init_data???
            serialized.data['username'],
            serialized.data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_openings(request):
    if request.method == 'GET':
        openings = Opening.objects.all()
        serialized = OpeningSerializer(openings, many=True)
        return Response(serialized.data)

    elif request.method == 'POST':
        deserialized = OpeningSerializer(data=request.data)
        if deserialized.is_valid():
            op = Opening(**deserialized.validated_data)
            link = OpeningToUser(person=request.user, opening=op)
            print("Deserialized: {}".format(deserialized))
            return Response(deserialized.data, status=status.HTTP_201_CREATED)
        return Response(deserialized.errors,
                status=status.HTTP_400_BAD_REQUEST)


#@api_view(['GET', 'POST'])
#@authentication_classes((TokenAuthentication,))
#@permission_classes((IsAuthenticated,))
#def bid(request):
#    if request.method == 'GET':
#        params = json.loads(request.body)
#        try:
#
#        bids = Bid.objects.all
