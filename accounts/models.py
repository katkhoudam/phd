# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-04-24 18:47:27
# @Last Modified by:   Your name
# @Last Modified time: 2023-04-24 22:37:36
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from .managers import CustomUserManager
# Create your models here.
class User(AbstractUser):
    email=models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone=models.CharField(null=True,max_length=255)
    REQUIRED_FIELDS=['username','phone','first_name','last_name']
    USERNAME_FIELD='email'

    def get_username(self):
        return self.email
class UserManager(CustomUserManager):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
