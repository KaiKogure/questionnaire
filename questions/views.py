from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from questions.models import Question
from titles.models import Title


class QuestionListView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        title_objects = Title.objects.filter(ask=True)
        
        #https://stackoverflow.com/questions/29587382/how-to-add-an-model-instance-to-a-django-queryset
        """
        queryset = Question.objects.none()
        for title_obj in title_onjects:
            question_objects = Question.objects.filter(title__id=title_obj.id)
            queryset = queryset.union(question_objects)
        question_objects = queryset
        context["question_objects"] = question_objects
        """

        # https://stackoverflow.com/questions/1042596/get-the-index-of-an-element-in-a-queryset
        for index, title_obj in enumerate(title_objects):
            question_objects = Question.objects.filter(title__id=title_obj.id)
            context_key = "objects"+str(index)
            context[context_key] = question_objects

        print(context)


        return render(request, "questions/list.html", context)
