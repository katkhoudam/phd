# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-04-24 18:52:12
# @Last Modified by:   Your name
# @Last Modified time: 2023-04-24 18:52:18
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username',
                  'first_name', 'last_name', 'phone')
