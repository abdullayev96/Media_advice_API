from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
     list_display = ['id', 'reference_number', 'verification_code', 'full_name', 'email',
                     'number','file', 'status', 'question', 'answers', 'created_at']



     search_fields = ['full_name']


admin.site.register(Question, QuestionAdmin)