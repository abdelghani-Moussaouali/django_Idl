from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import course,studentCourse
from .serializers import   CourseSerializer,StudentCourseSerializer
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

# get all StudentCourse
@api_view(['GET'])
def get_student_course(request):
    studentcourse = studentCourse.objects.all()
    serializer = StudentCourseSerializer(studentcourse, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_student_course(request):
    serializer = StudentCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "New student_course is added","student_course":serializer.data})
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_student_course(request, id):
    try:
        student_course_ins = studentCourse.objects.get(id=id)
    except studentCourse.DoesNotExist:
        return Response({"error": "student Course not found"}, status=404)
    student_course_ins.delete()
    return Response({"error": "student Course was deleted"}, status=200)