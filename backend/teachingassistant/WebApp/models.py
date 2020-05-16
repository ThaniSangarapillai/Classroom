from djongo import models
from django import forms
import datetime
# Create your models here.
# class BadWord(models.Model):
#     word = models.CharField(max_length=255)
#
#     class Meta:
#         abstract = True
#
# class BadWordForm(forms.ModelForm):
#     class Meta:
#         model = BadWord
#         fields = (
#             'word',
#         )

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    duedate = models.DateTimeField()

    class Meta:
        abstract = True

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = (
            'name', 'duedate'
        )



class Student(models.Model):
    name = models.CharField(max_length=100)
    discord_name = models.CharField(max_length=100)
    assignments = models.ArrayField(
        model_container=Assignment,
        model_form_class=AssignmentForm
    )

    class Meta:
        abstract = True

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'name', 'discord_name', 'assignments'
        )

class StringField(models.Model):
    word = models.CharField(max_length=50)
    assigned_by = models.EmbeddedField(
        model_container=Student,
        model_form_class=StudentForm
    )
    class Meta:
        abstract = True

class StringFieldForm(forms.ModelForm):
    class Meta:
        model = StringField
        fields = (
            'word', 'assigned_by'
        )

class AStudent(models.Model):
    name = models.CharField(max_length=100)
    discord_name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class AStudentForm(forms.ModelForm):
    class Meta:
        model = AStudent
        fields = (
            'name', 'discord_name'
        )

class AttendanceEntry(models.Model):
    student = models.EmbeddedField(
        model_container=AStudent,
        model_form_class=AStudentForm
    )
    presence = models.BooleanField(default=False)

    class Meta:
        abstract = True

class AttendanceEntryForm(forms.ModelForm):
    class Meta:
        model = AttendanceEntry
        fields = (
            'student', 'presence'
        )

class Attendance(models.Model):
    day = models.DateField(default=datetime.date.today)
    student_list = models.ArrayField(
        model_container=AttendanceEntry,
        model_form_class=AttendanceEntryForm
    )

    class Meta:
        abstract = True
# class CurrentDay(models.Model):
#     day = models.DateField()
#     attend_list = models.EmbeddedField(
#         model_container=Attendance,
#         model_form_class=AttendanceForm
#     )
#
#     class Meta:
#         abstract = True

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = (
            'day', 'student_list'
        )

class Classroom(models.Model):
    teacher = models.EmbeddedField(
        model_container=Student,
        model_form_class=StudentForm
    )

    students = models.ArrayField(
        model_container=Student,
        model_form_class=StudentForm
    )

    assignments = models.ArrayField(
        model_container=Assignment,
        model_form_class=AssignmentForm
    )

    filter_words = models.ArrayField(
        model_container=StringField,
        model_form_class=StringFieldForm
    )

    attendance = models.ArrayField(
        model_container=Attendance,
        model_form_class=AttendanceForm
    )

# class Words(models.Model):
#     _id = models.ObjectIdField()
#     words = models.ArrayField(
#         model_container=BadWord,
#         model_form_class=BadWordForm,
#         default=None
#     )
#
#     objects = models.DjongoManager()
