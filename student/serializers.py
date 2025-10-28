from rest_framework import serializers
from .models import student, uiversity

class UnivSerializer(serializers.ModelSerializer):
 class Meta:
   model = uiversity
   fields = ['id', 'name','location']

class StudentSerializer(serializers.ModelSerializer):
  # that's like a resource to define univ how it's look in response
  univ = UnivSerializer(read_only=True)
  
  univ_id = serializers.PrimaryKeyRelatedField(
      queryset=uiversity.objects.all(), 
      source='univ', 
      write_only=True, 
      required=True, 
  )

  class Meta:
        model = student
        fields = ['id', 'first_name', 'last_name', 'email','univ', 'univ_id']