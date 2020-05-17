from djongo import models
from django import forms
import datetime


# Create your models here.


class Assignment(models.Model):
    name = models.CharField(max_length=50)
    duedate = models.DateTimeField(default=datetime.datetime.now())


class Student(models.Model):
    name = models.CharField(max_length=100)
    discord_name = models.CharField(max_length=100)


class StringField(models.Model):
    word = models.CharField(max_length=50)
    created = models.DateTimeField(default=datetime.datetime.now())


class AttendanceEntry(models.Model):
    name = models.CharField(max_length=100)
    discord_name = models.CharField(max_length=100)
    presence = models.BooleanField(default=False)


class Attendance(models.Model):
    day = models.DateField(default=datetime.date.today)
    student_list = models.ArrayField(
        model_container=AttendanceEntry
    )


class Reminder(models.Model):
    date_time = models.DateTimeField(default=datetime.datetime.now())
    text = models.TextField(default="")


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    discord_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    initialized = models.BooleanField(default=False)

    students = models.ArrayField(
        model_container=Student
    )

    assignments = models.ArrayField(
        model_container=Assignment
    )

    filter_words = models.ArrayField(
        model_container=StringField
    )

    attendance = models.ArrayField(
        model_container=Attendance
    )

    reminders = models.ArrayField(
        model_container=Reminder
    )
