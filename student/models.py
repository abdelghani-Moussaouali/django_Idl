from django.db import models

class course(models.Model):
    name = models.CharField(max_length=30)
    instructor = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    schedule = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class studentCourse(models.Model):
    student_id = models.IntegerField()
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)
    def __str__(self):
        return self.student_id