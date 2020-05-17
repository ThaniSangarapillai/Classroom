from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'classroom', views.ClassroomViewSet, basename='discord')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('verify/', views.verify),
    path('students/', views.students),
    path('assignments/', views.assignments),
    path('filterwords/', views.filterwords),
    path('attendance/', views.attendance),
    path('reminders/', views.reminders),
    path('change/name/', views.modify_teacher_name),
    path('change/email/', views.modify_teacher_email),
    path('add/student/', views.add_student),
    path('remove/student/', views.remove_student),
    path('add/assn/', views.add_assignment),
    path('remove/assn/', views.remove_assignment),
    path('modify/assn/', views.modify_assignment),
    path('add/word/', views.add_word),
    path('remove/word/', views.remove_word),
    path('add/attendance/', views.attendance_bulk),
    path('modify/attendance/', views.modify_attendance),
    path('add/reminder/', views.add_reminder),
    path('modify/reminder/', views.modify_reminder),
    path('remove/reminder/', views.remove_reminder),
    path('remove/reminders/', views.clean_reminders),
    path('initialized/', views.initialized),
    path('initialize/', views.initialize)
]
