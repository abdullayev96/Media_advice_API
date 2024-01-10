from django.contrib import admin


from .models import Questions


class QuestionsAdmin(admin.ModelAdmin):
     list_display = ['id', 'questions','answers', 'created_at']



     search_fields = ['questions']


admin.site.register(Questions, QuestionsAdmin)
