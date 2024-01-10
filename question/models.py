from django.db import models
from baseapp.models import BaseModel
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import os
from datetime import datetime

from pathlib import Path
from django.core.files import File
from django.core.files.base import ContentFile




def validate_number(value):
    if value:
        if value > 100000:
            raise ValidationError("The number of team per pool is <100000. Please try again.")
    return value


def validate_geeks_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")


def validate_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('You must enter .pdf, .doc, .docx file ')



STATUS_ACTIVATE = [
    ("new", "new"),
    ("answered", "Answered"),
    ("rejected","Rejected")
]



class Question(BaseModel):
    NEW = "new"
    EXECUTION = "execution"
    COMPLETED = "completed"

    STATUS_CHOICES = (
        (NEW, 'new'),
        (EXECUTION, 'execution'),
        (COMPLETED, 'completed'),
    )

    reference_number = models.SmallIntegerField(validators=[validate_number])
    verification_code = models.CharField(max_length=10)
    full_name = models.CharField(max_length=200, verbose_name="To'liq ismi:")
    email = models.EmailField(unique=True, validators=[validate_geeks_mail])
    number = models.CharField(max_length=20, verbose_name="Nomerizni kiriting:")
    file = models.FileField(upload_to="yes/", validators=[validate_file])
    status  = models.CharField(max_length=9, choices=STATUS_CHOICES, verbose_name="Status:", default="new")
    question = models.TextField(verbose_name="Savol matni:")
    answers = models.FileField(upload_to="yes/", validators=[validate_file])



    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Savollar_"


