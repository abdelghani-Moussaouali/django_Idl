import graphene
from graphene_django import DjangoObjectType

from .models import student

class StudentType(DjangoObjectType):
    class Meta:
        model = student
        fields = ("id","first_name", "last_name", "email")

class Query(graphene.ObjectType):
    student = graphene.List(StudentType,)

    def resolve_student(root, info):
        qs = student.objects.all()
        
        return qs
    
schema = graphene.Schema(query=Query)
