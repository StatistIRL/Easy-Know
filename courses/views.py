from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class CatalogView(View):
    def get(self, request):
        context = {}
        return render(
            request=request, template_name="courses/catalog.html", context=context
        )
