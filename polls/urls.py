from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_questions, name='questions'),
    path('choices/<int:question_id>/', views.display_choices, name='choices'),
    path('vote/<int:question_id>', views.register_vote, name='vote'),
    path('results/<int:question_id>', views.display_results, name='results'),
]