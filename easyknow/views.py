from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class IndexPageView(View):
    def get(self, request):
        context = {}
        return render(
            request=request, template_name="easyknow/index.html", context=context
        )
