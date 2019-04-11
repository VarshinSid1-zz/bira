from django.contrib import admin
from .models import Projectlist, User, Issue
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'date_created', 'date_modified')


admin.site.register(Projectlist, ProjectAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_status')


admin.site.register(User, UserAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ['issue_id', 'issue_title', 'assignee', 'project_assigned', 'type', 'sprint', 'status',
                    'issue_date_created', 'issue_date_modified']


admin.site.register(Issue, IssueAdmin)
#
#
# class AssignAdmin(admin.ModelAdmin):
#     list_display = ('issue_id', 'user_id')
#
# admin.site.register(Assign_Issue, AssignAdmin)