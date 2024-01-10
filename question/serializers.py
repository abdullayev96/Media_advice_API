from rest_framework import serializers
from .models import  Question



class QuestionSerializer(serializers.ModelSerializer):
     class Meta:
          model = Question
          fields = ['full_name', 'email', 'number', 'file', 'question']



class CheckSerializer(serializers.ModelSerializer):
     class Meta:
          model = Question
          fields = ['reference_number', 'verification_code']


class QuestionAnswerSerializer(serializers.ModelSerializer):
     class Meta:
          model = Question
          fields = ['reference_number','created_at','full_name', 'email', 'file','question', 'status', 'answers']
