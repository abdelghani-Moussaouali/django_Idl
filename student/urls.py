
from django.urls import path
from graphene_django.views import GraphQLView

from .schema import schema  

from . import views
urlpatterns = [
  
  # course routes
  path('course/add',view=views.add_course,name='add_course'),
  path('course/all',view=views.get_all_courses,name='get_all_courses'),
  path('course/delete/<int:id>',view=views.delete_course,name='delete_course'),
  path('course/update/<int:id>/',view=views.update_course,name='update_course'),
  path('course/search',view=views.search_courses,name='search_courses'),
  
 
 
 
  path('StudentCourse/',view=views.get_student_course,name='get_student_course'),
  path('StudentCourse/add/',view=views.add_student_course,name='add_student_course'),
  path('StudentCourse/delete/<int:id>',view=views.delete_student_course,name='delete_student_course'),
 
 
  path("graphql/", GraphQLView.as_view(schema=schema, graphiql=True)),
 
]
