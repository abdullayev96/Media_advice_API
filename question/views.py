from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Question
from .serializers import *
from rest_framework import status
import random
import string


def generate_random_string(length):
          characters = string.ascii_letters + string.digits
          verification_code = ''.join(random.choice(characters) for _ in range(length))
          return verification_code


class QuestionAPI(APIView):
     def post(self, request):
          try:
             reference_number = random.randint(10000, 99999)
             verification_code = generate_random_string(10)


             serializer = QuestionSerializer(data=request.data, context={'request': self.request})
             serializer.is_valid(raise_exception=True)
             serializer.save(reference_number=reference_number
                                    , verification_code=verification_code, status=Question.NEW)

             return Response({"Savol tartib raqami": reference_number, "Tekshirish kodi": verification_code})

          except Exception as e:
                    print(e)


          return Response({"status":status.HTTP_404_NOT_FOUND})




class AnswerAPI(APIView):
     def post(self, request, *args, **kwargs):
          try:
               serializers = CheckSerializer(data=request.data, context={'request': self.request})
               if serializers.is_valid(raise_exception=True):
                    reference_number=serializers.data.get('reference_number')
                    verification_code = serializers.data.get('verification_code')

                    send = Question.objects.filter(reference_number=reference_number,verification_code=verification_code)
                    serializer = QuestionAnswerSerializer(send, many=True, context={'request': self.request})

                    return Response(serializer.data)

               else:
                    return Response(serializers.errors, status=400)

          except Exception as e:
                    print(e)

          return Response({"status":status.HTTP_404_NOT_FOUND})


     # def post(self, request, *args, **kwargs):
     #     reference_number = self.request.POST.get("reference_number")
     #     verification_code = self.request.POST.get("verification_code")
     #     send = SendUser.objects.filter(reference_number=reference_number, verification_code=verification_code)
     #     serializer = SendAnswerSerializer(send, many=True)
     #
     #
     #     return Response(serializer.data)
