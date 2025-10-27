from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student , Univ
from .serializers import StudentSerializer , UnivSerializer 

@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "New student is added"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_univ(request):
    Univs = Univ.objects.all()
    serializer = UnivSerializer(Univs, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def add_univ(request):
    serializer = UnivSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "New univ is added"})
    return Response(serializer.errors, status=400)