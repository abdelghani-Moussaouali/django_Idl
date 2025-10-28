from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('students/',view=views.get_all_students,name='get_all_students'),
  path('students/add/',view=views.add_student,name='add_student'),
  path('univ/add/',view=views.add_univ,name='add_univ'),
  path('univ/',view=views.get_all_univ,name='get_all_univ'),
]
