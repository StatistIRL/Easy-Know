from django.urls import include, path
from . import views

app_name = "courses"

urlpatterns = [
    path("catalog/", views.CatalogView.as_view(), name="catalog"),
    path("course/<slug:slug>/", include("courses.course_urls")),
]
