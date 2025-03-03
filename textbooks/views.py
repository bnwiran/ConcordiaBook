from django.shortcuts import render

from textbooks.models import Textbook


# Create your views here.
def available_textbook_list(request, course_id):
    course_id = course_id.upper()
    all_textbooks = Textbook.objects.filter(course=course_id, availability=True)
    context = {"all_textbooks": all_textbooks, "course_id": course_id}
    return render(request, "textbooks/available_textbook_list.html", context=context)
