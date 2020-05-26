from django.urls import path
from questions.views import QuestionListView



urlpatterns = [
    path("list/", QuestionListView.as_view() , name="QuestionListView"),
]
