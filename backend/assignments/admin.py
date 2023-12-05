from django.contrib import admin
from assignments.models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    fields = ("first_term", "second_term", "sum")
    list_display = ("first_term", "second_term")


admin.site.register(Assignment, AssignmentAdmin)