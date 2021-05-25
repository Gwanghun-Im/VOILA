from datetime import date
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from django.core import serializers

from .serializers import UserSerializer, UserLoginSerializer, UserProfileSerializer
from .models import User

import jwt
from django.conf import settings

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'})
		
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
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
            'email':serializer.data['email'],
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
    userserializer = UserProfileSerializer(user)
    review = user.review_set.all()
    review_list = serializers.serialize('json',review)
    data={
        'user':userserializer.data,
        'review':review_list
    }
    return Response(data)

### 카카오 로그인
import urllib
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # 프로젝트/accounts

with open(os.path.join(BASE_DIR, 'server\secrets.json'), 'rb') as secret_file:
    secrets = json.load(secret_file)

# code 요청
def kakao_login(request):
    app_rest_api_key = secrets['KAKAO']["REST_API_KEY"]
    redirect_uri =  secrets['KAKAO']["MAIN_DOMAIN"] + "/accounts/login/kakao/callback/"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )
    
import requests
from django.shortcuts import redirect 
from .models import User


class KakaoException(Exception):
    pass


# access token 요청 함수
@api_view(['GET'])
def kakao_callback(request):
    try:
        app_rest_api_key = secrets['KAKAO']["REST_API_KEY"]
        redirect_uri = secrets['KAKAO']["MAIN_DOMAIN"] + "/accounts/login/kakao/callback/"
        user_token = request.GET.get("code")

        # post request
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}"
        )
        token_response_json = token_request.json()
        error = token_response_json.get("error", None)
        print(token_response_json)
        # if there is an error from token_request
        if error is not None:
            raise KakaoException()
        access_token = token_response_json.get("access_token")
		
        # post request
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()

        # parsing profile json
        kakao_account = profile_json.get("kakao_account")
        email = kakao_account.get("email", None)
        if email is None:
            raise KakaoException()   # 이메일은 필수제공 항목이 아니므로 수정 필요 (비즈니스 채널을 연결하면 검수 신청 후 필수 변환 가능)
        profile = kakao_account.get("profile")
        nickname = profile.get("nickname")
        profile_image = profile.get("thumbnail_image_url")   # 사이즈 'thumbnail_image_url' < 'profile_image_url'
        print('email', email)
        print('image', profile_image)
        print(kakao_account)
        try:   
            user_in_db = User.objects.get(email=email)
            # 프로필 정보 업데이트
            User.objects.filter(email=email).update(realname=nickname,
                                                    email=email,
                                                    profile_image=profile_image,
                                                    is_active=True
                                                    )

        except User.DoesNotExist:
            data = {'code': user_token, 'access_token': access_token}
            User(email=email,realname=nickname,profile_image=profile_image,is_active=True).save()
        print(access_token)
        
        response = {
            'success': True,
            'token': access_token
        }
        return Response(response, status=status.HTTP_200_OK)

    except KakaoException:
        print(KakaoException)
        return redirect("http://127.0.0.1:8080/accounts/login")
