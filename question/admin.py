from django.contrib import admin
from .models import Question,Comment
# Register your models here.
class QuestionModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Comment)
