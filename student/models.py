from django.db import models
from django.contrib.auth.models import User
class student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    univ = models.ForeignKey('uiversity',on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    
    
class course(models.Model):
    name = models.CharField(max_length=30)
    instructor = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    schedule = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name
    
    
class studentCourse(models.Model):
    student_id = models.ForeignKey('student',on_delete=models.CASCADE)
    course_id = models.ForeignKey('course',on_delete=models.CASCADE)
    
    

class uiversity(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name