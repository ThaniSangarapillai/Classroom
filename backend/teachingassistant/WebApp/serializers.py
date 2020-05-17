from django.contrib.auth.models import User, Group
from .models import Classroom, Student, Assignment, StringField, AttendanceEntry, Attendance, Reminder
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'discord_name')

class StringFieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StringField
        fields = ('word', 'created')

class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        fields = ('name', 'duedate')

class ReminderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reminder
        fields = ('date_time', 'text')

class AttendanceEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AttendanceEntry
        fields = ('name', 'discord_name', 'presence')

class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    student_list = AttendanceEntrySerializer(many=True, required=False, read_only=False)
    class Meta:
        model = Attendance
        fields = ('day', 'student_list')

class ClassroomSerializer(serializers.HyperlinkedModelSerializer):
    students = StudentSerializer(many=True, required=False, read_only=False)
    assignments = AssignmentSerializer(many=True, required=False, read_only=False)
    filter_words = StringFieldSerializer(many=True, required=False, read_only=False)
    attendance = AttendanceSerializer(many=True, required=False, read_only=False)
    reminders = ReminderSerializer(many=True, required=False, read_only=False)
    class Meta:
        model = Classroom
        fields = ('pk', 'name', 'discord_name', 'email', 'initialized', 'students', 'assignments', 'filter_words', 'attendance', 'reminders')

    # def create(self, validated_data):
    #     students = validated_data.pop('students', None)
    #     assignments = validated_data.pop('assignments', None)
    #     filter_words = validated_data.pop('filter_words', None)
    #     attendance = validated_data.pop('attendance', None)
    #     reminders = validated_data.pop('reminders', None)
    #     classroom = Classroom(**validated_data)
    #     classroom.save()
    #     for item in students:
    #         Student.objects.create(**item)
    #
    # def update(self, instance, validated_data):
    #     nested_serializer = self.fields['students']
    #     nested_instance = instance.students
