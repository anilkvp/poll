
from questions import views
from django.urls import path

urlpatterns = [
    path('save_poll/', views.save_poll, name='save_poll'),
    path('poll_summary/<int:question_id>', views.summary_view, name='poll_summary')
]
