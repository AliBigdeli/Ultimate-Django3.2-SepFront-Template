from rest_framework.response import Response
from rest_framework import generics, status, views, mixins
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings

class DemoApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "author":"Ali Bigdeli",
            "email":"bigdeli.ali3@gmail.com"
            }
        return Response(data ,status=status.HTTP_200_OK)