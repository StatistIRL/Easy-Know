from django.shortcuts import render
from django.views.generic import DetailView, View
from courses.models import Course
from courses.services.courses import get_all_courses

# Create your views here.


class CatalogView(View):
    def get(self, request):
        courses = get_all_courses()
        context = {"courses": courses}
        return render(
            request=request, template_name="courses/catalog.html", context=context
        )


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course/home.html"
    context_object_name = "course"
