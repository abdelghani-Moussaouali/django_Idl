from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student, uiversity
from .serializers import StudentSerializer , UnivSerializer 
# add student
@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "New student is added","student":serializer.data})
    return Response(serializer.errors, status=400)

# update student
@api_view(['PUT'])
def update_student(request, id):
    try:
        student = student.objects.get(id=id)
    except student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()  
        return Response({"message": "Student updated successfully","student":serializer.data})
    return Response(serializer.errors, status=400)

# delete student
@api_view(['PUT'])
def update_student(request, id):
    try:
        student = student.objects.get(id=id)
    except student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()  
        return Response({"message": "Student updated successfully","student":serializer.data})
    return Response(serializer.errors, status=400)

# get all student
@api_view(['GET'])
def get_all_students(request):
    students = student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_univ(request):
    Univs = uiversity.objects.all()
    serializer = UnivSerializer(Univs, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def add_univ(request):
    serializer = UnivSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "New university is added"})
    return Response(serializer.errors, status=400)