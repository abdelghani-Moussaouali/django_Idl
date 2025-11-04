from rest_framework import serializers
from .models import student, uiversity,course,studentCourse

class UnivSerializer(serializers.ModelSerializer):
 class Meta:
   model = uiversity
   fields = ['id', 'name','location']

class StudentSerializer(serializers.ModelSerializer):
  # that's like a resource to define univ how it's look in response
  # univ = UnivSerializer(read_only=True)
  # univ_id = serializers.PrimaryKeyRelatedField(
  #     queryset=uiversity.objects.all(), 
  #     source='univ', 
  #     write_only=True, 
  #     required=True, 
  # )

  class Meta:
    model = student
    fields =('__all__')

class CourseSerializer(serializers.ModelSerializer):
 class Meta:
   model = course
   fields = ('__all__')


class StudentCourseSerializer(serializers.ModelSerializer):
 class Meta:
   model = studentCourse
   fields = ('__all__')