from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  
  # course routes
  path('course/add/',view=views.add_course,name='add_course'),
  path('course/',view=views.get_all_courses,name='get_all_courses'),
  path('course/<int:id>/delete/',view=views.delete_course,name='delete_course'),
  path('course/<int:id>/update/',view=views.update_course,name='update_course'),
  path('course/search',view=views.search_courses,name='search_courses'),
  
  # student routes
  path('student/add/',view=views.add_student,name='add_student'),
  path('student/',view=views.get_all_student,name='get_all_student'),
  path('student/<int:id>/delete/',view=views.delete_student,name='delete_student'),
  path('student/<int:id>/update/',view=views.update_student,name='update_student'),
 
]
