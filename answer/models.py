from django.db import models
from baseapp.models import BaseModel



class Questions(BaseModel):
     questions = models.CharField(max_length=5000, verbose_name="Savollar:")
     answers = models.TextField(verbose_name="Javoblar:")


     def __str__(self):
         return self.questions


     class Meta:
          verbose_name = "Savollar_"

