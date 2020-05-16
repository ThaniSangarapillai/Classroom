from django.contrib import admin
from .models import Classroom
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Classroom)
#admin.site.register(User)
#admin.site.register(Entry)