from django.db.models import fields
from rest_framework import serializers
from .models import Helpline, Report

class HelplineList(serializers.ModelSerializer):
    class Meta:
        model = Helpline
        fields = '__all__'
    
class ReportList(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
