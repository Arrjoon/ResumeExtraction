from django.contrib import admin
from .models import Job_Description,Resume_Description

# Register your models here.
@admin.register(Resume_Description)
class ResumeDescriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'location', 'email_address', 'company_working_at', 'get_skills_display','degree', 'college_name', 'graduation_year', 'experience', 'university')
    list_filter = ('company_working_at', 'degree', 'graduation_year', 'experience', 'university')
    search_fields = ('name', 'designation', 'location', 'email_address', 'college_name', 'skills')

    def get_skills_display(self, obj):
        return ', '.join(obj.get_skills_list())
    get_skills_display.short_description = 'Skills'

admin.site.register(Job_Description)
# admin.site.register(Resume_Description)