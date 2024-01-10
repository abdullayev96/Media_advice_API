from django.urls import path
from .views import QuestionAPI, AnswerAPI

urlpatterns  = [
         path('', QuestionAPI.as_view(), name="question"),
         path('answers/', AnswerAPI.as_view(), name="answers")


]