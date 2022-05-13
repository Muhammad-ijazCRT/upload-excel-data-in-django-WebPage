from rest_framework import serializers
from polls.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'address']
