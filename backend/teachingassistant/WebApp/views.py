from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer, ClassroomSerializer
from django.contrib.auth.decorators import login_required
from .models import Classroom, Student, Assignment, Attendance, StringField, Reminder
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserCreationForm()
    return render(request,'WebApp/registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'WebApp/login.html', {})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

#@csrf_exempt
class ClassroomViewSet(viewsets.ModelViewSet):
    serializer_class = ClassroomSerializer
    permission_classes = [permissions.IsAuthenticated]

    # @action(detail=False, methods=['post'], name="Receive User")
    # def verify(self, request, pk=None):
    #     print(request.data)
    #     return Response({'status':'ok'})

    def get_queryset(self):
        print(self.request.user.email)
        return Classroom.objects.all()

@csrf_exempt
@login_required()
def verify(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.filter(discord_name=data["discord_name"], email=data["email"])
            serializer = ClassroomSerializer(snippets, many=True)
            if serializer.data != []:
                return JsonResponse(serializer.data, safe=False)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def students(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.filter(discord_name=data["discord_name"], email=data["email"])
            serializer = ClassroomSerializer(snippets, many=True)
            if serializer.data != []:
                return JsonResponse(serializer.data[0]["students"], safe=False)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def assignments(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.filter(discord_name=data["discord_name"], email=data["email"])
            serializer = ClassroomSerializer(snippets, many=True)
            if serializer.data != []:
                return JsonResponse(serializer.data[0]["assignments"], safe=False)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def filterwords(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.filter(discord_name=data["discord_name"], email=data["email"])
            serializer = ClassroomSerializer(snippets, many=True)
            if serializer.data != []:
                return JsonResponse(serializer.data[0]["filter_words"], safe=False)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def attendance(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.filter(discord_name=data["discord_name"], email=data["email"])
            serializer = ClassroomSerializer(snippets, many=True)
            if serializer.data != []:
                return JsonResponse(serializer.data[0]["attendance"], safe=False)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def reminders(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.filter(discord_name=data["discord_name"], email=data["email"])
            serializer = ClassroomSerializer(snippets, many=True)
            if serializer.data != []:
                return JsonResponse(serializer.data[0]["reminders   "], safe=False)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

def modify_teacher_name(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            snippets.name = data["name"]
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

def modify_teacher_email(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "name" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], name=data["name"])
            snippets.email = data["email"]
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

def add_student(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            temp_stud = Student(**data["student"])
            snippets.students.append(temp_stud)
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

def remove_student(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            temp_stud = Student(**data["student"])
            for x in list(snippets.students):
                if x.name == temp_stud.name and x.discord_name == temp_stud.discord_name:
                    snippets.students.remove(x)
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)