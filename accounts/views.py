# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-04-24 18:47:27
# @Last Modified by:   Your name
# @Last Modified time: 2023-04-24 18:53:13
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data="This page only for logged person", status=status.HTTP_200_OK)
