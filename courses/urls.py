from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [path("catalog/", views.CatalogView.as_view(), name="catalog")]
