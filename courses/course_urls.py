from django.urls import path

from courses import views

urlpatterns = [path("home/", views.CourseDetail.as_view(), name="home")]
