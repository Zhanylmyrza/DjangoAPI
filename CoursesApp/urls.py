from django.urls import path
from CoursesApp import views
from CoursesApp.views import CourseApi
from CoursesApp.views import CourseDetailView

urlpatterns = [
    # path("course",views.courseApi.as_view()),
    path("course", views.CourseApi.as_view()),
    # path('course/$', views.courseApi.as_view()),
    path("course/<int:id>", CourseDetailView.as_view()),
]
