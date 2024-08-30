from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import User, Group
from polls.models import Choice, Question


class CustomAdminSite(admin.AdminSite):
    site_header = 'Curso de python Admin'


admin_site = CustomAdminSite()
admin_site.register(Choice)
admin_site.register(Question)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)

