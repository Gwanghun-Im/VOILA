from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render, get_list_or_404, get_object_or_404

from .serializers import UserSerializer, UserLoginSerializer, UserProfileSerializer
from .models import User

import jwt
from django.conf import settings

@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'})
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # print(user.password)
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None": # email required
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)
        response = {
            'success': True,
            'token': serializer.data['token'] # 시리얼라이저에서 받은 토큰 전달
        }
        return Response(response, status=status.HTTP_200_OK)

@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def profile(request):
    token = request.headers['Authorization'].split()[1]
    SECRET_KEY = settings.SECRET_KEY
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    user = get_object_or_404(User, email=payload["email"])
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)