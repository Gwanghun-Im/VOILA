from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, UserManager
from rest_framework.decorators import parser_classes

class User(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(max_length=30)
    email = models.EmailField('이메일', unique=True)
    password = models.CharField('비밀번호', max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    realname = models.CharField('이름', blank=True, max_length=50)
    nickname = models.CharField('닉네임', blank=True, max_length=50)
    address = models.CharField('주소', blank=True, max_length=200)
    phone = models.CharField('휴대폰번호', blank=True, max_length=50)
    date_of_birth = models.DateField('생년월일', blank=True, null=True)
    profile_image = models.ImageField('프로필사진', blank=True, null=True)

