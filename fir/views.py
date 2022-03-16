from django.shortcuts import render
from rest_framework.response import Response
from .models import Helpline, Report
from .serializers import HelplineList, ReportList
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class HelplineView(APIView):
    def get(self, request, format=None):
        contact = Helpline.objects.all()
        serializer = HelplineList(contact, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HelplineList(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportView(APIView):
    def get(self, request, format=None):
        contact = Report.objects.all()
        serializer = ReportList(contact, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HelplineList(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)