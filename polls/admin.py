from django.contrib import admin
from .models import Question,Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
  #specifies that the publication date should come before the question text
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# Register your models here.
