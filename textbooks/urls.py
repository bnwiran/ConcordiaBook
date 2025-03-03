from django.urls import path
from django.views.generic import TemplateView

from textbooks import views as textbook_views

urlpatterns = [
    path("<str:course_id>", textbook_views.available_textbook_list, name="available_textbook_list"),
    path("", TemplateView.as_view(template_name="textbooks/textbooks_home.html"), name="textbooks_home"),
]
