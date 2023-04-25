# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-04-24 18:56:44
# @Last Modified by:   Your name
# @Last Modified time: 2023-04-24 18:56:46
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


@api_view(['GET'])
def index(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = "Clock in server is live current time is"
    return Response(data=message+date, status=status.HTTP_200_OK)
