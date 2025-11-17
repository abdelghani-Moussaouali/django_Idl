import graphene
from graphene_django import DjangoObjectType

from .models import course


        
class CourseType(DjangoObjectType):
    class Meta:
        model = course
        fields = ("id","name", "instructor", "category", "schedule" )


class Query(graphene.ObjectType):
   
    courses = graphene.List(CourseType)

  
      
    def resolve_courses(root, info):
        qs = course.objects.all() 
        return qs
    
schema = graphene.Schema(query=Query)
