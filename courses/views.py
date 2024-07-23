from django.shortcuts import render
from django.views.generic import View
from courses.services.courses import get_all_courses

# Create your views here.


class CatalogView(View):
    def get(self, request):
        courses = get_all_courses()
        context = {"courses": courses}
        return render(
            request=request, template_name="courses/catalog.html", context=context
        )
