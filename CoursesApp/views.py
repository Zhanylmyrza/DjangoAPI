from CoursesApp.models import Category, Branch, Contact, Course
from CoursesApp.serializer import CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class CourseApi(APIView):
    def get(self, request):
        query_set = Course.objects.all()
        return Response({"Data": CourseSerializer(query_set, many=True).data})

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


class CourseDetailView(APIView):
    def get(self, request, id=None):
        # query_set=Course.objects.all()
        # return Response({'Data':CourseSerializer(query_set,many=True).data})
        courseId = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(courseId)
        return Response(serializer.data)

    def delete(self, request, id=None):
        # print(request.GET['id'])
        item = Course.objects.get(id=id).delete()
        # item = self.model.objects.get(item_name=request.GET['id'])
        # item.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"id": str(id) + " delete"})


# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse

# from CoursesApp.models import Category,Branch,Contact,Course
# from CoursesApp.serializer import CategorySerializer, BranchSerializer,ContactSerializer,CourseSerializer

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# # Create your views here.

# @api_view(['GET,POST'])
# def courseApi(request,id=0):
#   if request.method == 'POST':
#     return Response(CourseSerializer(data=request.data))
#     if courses_serializer.is_valid():
#       courses_serializer.save()
#       return Response({'post':courses_serializer.data})
# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "courses_serializer.data", "data": request.data})
#     return Response({"message": "Hello, world!"})


# @csrf_exempt
# def courseApi(request,id=0):
#   if request.method=='GET':
#     courses=Course.objects.all()
#     courses_serializer=CourseSerializer(courses,many=True)
#     return JsonResponse(courses_serializer.data,safe=False)
#   elif request.method=='POST':
#     course_data=JSONParser().parse(request.data)
#     courses_serializer=CourseSerializer(data=course_data)
#     if courses_serializer.is_valid():
#       courses_serializer.save()
#       return JsonResponse("Added successfully",safe=False)
#     return JsonResponse("Failed to Add",safe=False)
#   elif request.method=='PUT':
#     course_data=JSONParser.parse(request)
#     course=Course.object.get(CourseId=course_data['CourseId'])
#     courses_serializer=CourseSerializer(course,data=course_data)
#     if courses_serializer.is_valid():
#       courses_serializer.save()
#       return JsonResponse("Update Successfully",safe=False)
#     return JsonResponse("Failed to Update")
#   elif request.method=='DELETE':
#     course=Course.objects.get(CourseId=id)
#     course.delete()
#     return JsonResponse("Delete Successfully",safe=False)
