from django.contrib import admin
from polls.models import Student, UploadCsv
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address')


@admin.register(UploadCsv)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'textfile')
