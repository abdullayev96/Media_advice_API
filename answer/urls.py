from django.urls import path
from .views import *


urlpatterns = [
          path("", QuestionsAPI.as_view())

]