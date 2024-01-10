from rest_framework import serializers
from .models import *


class AnswerSerializer(serializers.ModelSerializer):
     class Meta:
          model = Questions
          fields  = ['id', 'questions', 'answers']



