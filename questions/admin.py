from django.contrib import admin
from questions.models import Question, Poll


admin.site.register(Question)
admin.site.register(Poll)