from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, ClassroomSerializer
from django.contrib.auth.decorators import login_required
from .models import Classroom, Student, Assignment, Attendance, StringField, Reminder, AttendanceEntry
from django.views.decorators.csrf import csrf_exempt
import json, datetime


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
    return render(request, 'WebApp/registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
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


# @csrf_exempt
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


# @csrf_exempt
# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def verify(request):
    #print(request.META['HTTP_AUTHORIZATION'])
    # content = {
    #     'user': request.user,  # `django.contrib.auth.User` instance.
    #     'auth': request.auth,  # None
    # }
    # print(content)
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.filter(discord_name=data["discord_name"], email=data["email"])
            serializer = ClassroomSerializer(snippets, many=True)
            if serializer.data != []:
                return JsonResponse(serializer.data, safe=False)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
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


# @csrf_exempt
# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
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


# @csrf_exempt
# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
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


# @csrf_exempt
# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
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


# @csrf_exempt
# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def reminders(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.filter(discord_name=data["discord_name"], email=data["email"])
            serializer = ClassroomSerializer(snippets, many=True)
            if serializer.data != []:
                return JsonResponse(serializer.data[0]["reminders"], safe=False)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
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

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
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

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
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

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
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

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def add_assignment(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            data["assignment"]["duedate"] = datetime.datetime.strptime(data["assignment"]["duedate"],
                                                                       '%Y-%m-%d %H:%M:%S')
            temp_stud = Assignment(**data["assignment"])
            snippets.assignments.append(temp_stud)
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def modify_assignment(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            change_name = False
            if "old_name" in data["assignment"]:
                change_name = True
            for x in list(snippets.assignments):
                if not change_name and x.name == data["assignment"]["name"]:
                    x.duedate = datetime.datetime.strptime(data["assignment"]["duedate"], '%Y-%m-%d %H:%M:%S')
                elif change_name and x.name == data["assignment"]["old_name"]:
                    x.name = data["assignment"]["name"]
                    x.duedate = datetime.datetime.strptime(data["assignment"]["duedate"], '%Y-%m-%d %H:%M:%S')
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def remove_assignment(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            temp_stud = Assignment(**data["assignment"])
            for x in list(snippets.assignments):
                if x.name == temp_stud.name:
                    snippets.assignments.remove(x)
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def add_word(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            temp_stud = StringField(created=datetime.datetime.now(), **data["word"])
            snippets.filter_words.append(temp_stud)
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def remove_word(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            for x in list(snippets.filter_words):
                if x.word == data["word"]["word"]:
                    snippets.filter_words.remove(x)
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def attendance_bulk(request):
    unregistered = []
    if request.method == "POST":
        data = JSONParser().parse(request)
        change = False
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            for x in snippets.attendance:
                print(str(x.day), str(datetime.date.today()))
                if str(x.day) == str(datetime.date.today()):
                    temp_attend = x
                    change = True
                    break
            else:
                temp_attend = Attendance(day=datetime.date.today(), student_list=list())
                change = False

            for x in data["student_list"]:
                print(x)
                for y in snippets.students:
                    if y.discord_name == x["discord_name"]:
                        name = y.name
                        break
                else:
                    if x["presence"]:
                        unregistered.append(x["discord_name"])
                    continue

                temp_stud = AttendanceEntry(name=name,**x)
                print(temp_stud)
                for x in temp_attend.student_list:
                    if x.discord_name == temp_stud.discord_name:
                        break
                else:
                    temp_attend.student_list.append(temp_stud)

            if not change and len(temp_attend.student_list) != 0:
                snippets.attendance.append(temp_attend)
            snippets.save()
            print(snippets)
            return JsonResponse({"unregistered": unregistered}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def modify_attendance(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            for x in list(snippets.attendance):
                if str(x.day) == str(data["day"]):
                    for y in x.student_list:
                        if y.name == data["student"]["name"] and y.discord_name == data["student"]["discord_name"]:
                            y.presence = data["student"]["presence"]
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

def add_reminder(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            data["reminder"]["date_time"] = datetime.datetime.strptime(data["reminder"]["date_time"], '%Y-%m-%d %H:%M:%S')
            temp_stud = Reminder(**data["reminder"])
            snippets.reminders.append(temp_stud)
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

def modify_reminder(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            data["reminder"]["date_time"] = datetime.datetime.strptime(data["reminder"]["date_time"],
                                                                       '%Y-%m-%d %H:%M:%S')
            snippets.reminders[data["reminder"]["pk"]] = Reminder(**data["reminder"])
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

def clean_reminders(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            for x in list(snippets.reminders):
                if datetime.datetime.now() > x.date_time:
                    snippets.reminders.remove(x)
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

def remove_reminder(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            #temp_stud = Reminder(**data["reminder"])
            # for x in list(snippets.reminders):
            #     if x.date_time == temp_stud.date_time and x.text == temp_stud.text:
            #         snippets.reminders.remove(x)
            del snippets.reminders[data["pk"]]
            snippets.save()
            print(snippets)
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

def initialized(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            return JsonResponse({"initialized":snippets.initialized}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)

def initialize(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        if "discord_name" in data and "email" in data:
            snippets = Classroom.objects.get(discord_name=data["discord_name"], email=data["email"])
            snippets.initialized = True
            snippets.save()
            return JsonResponse({}, status=status.HTTP_200_OK)

    return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)
