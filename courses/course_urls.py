from django.urls import path

from courses import views

urlpatterns = [path("home/", views.CourseDetailView.as_view(), name="home")]
