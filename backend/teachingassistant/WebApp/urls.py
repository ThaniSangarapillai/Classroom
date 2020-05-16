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
]