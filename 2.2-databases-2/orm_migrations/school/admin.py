from django.contrib import admin

from .models import Student, Teacher

# class MembershipInline(admin.TabularInline):
#     model = Student.teachers.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    #list_display = ['name', 'teachers', 'group']
    #inlines = [MembershipInline]
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    #list_display = ['name', 'subject']
    #inlines = [MembershipInline]
    pass  

