from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student, uiversity,course,studentCourse
from .serializers import StudentSerializer , UnivSerializer ,CourseSerializer,StudentCourseSerializer
from django.db.models import Q
# add course
@api_view(['POST'])
def add_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "New course is added","course":serializer.data})
    return Response(serializer.errors, status=400)

# get all course
@api_view(['GET'])
def get_all_courses(request):
    courses = course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)



# delete course
@api_view(['DELETE'])
def delete_course(request, id):
    try:
        course_ins = course.objects.get(id=id)
    except course.DoesNotExist:
        return Response({"error": "course not found"}, status=404)
    course_ins.delete()
    return Response({"error": "course was deleted"}, status=200)

# update cours
@api_view(['PUT'])
def update_course(request, id):
    try:
        course_ins = course.objects.get(id=id)
    except course.DoesNotExist:
        return Response({"error": "course not found"}, status=404)

    serializer = CourseSerializer(course_ins, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()  
        return Response({"message": "course updated successfully","course":serializer.data})
    return Response(serializer.errors, status=400)


# search courses by name,category,instructor
@api_view(['GET'])
def search_courses(request):
    query = request.GET.get('q', '')
    courses = course.objects.filter(
        Q(name=query) |
        Q(category=query) |
        Q(instructor=query)
    )
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

