from django.contrib import admin
from .models import Project, ProjectToMember


class MembershipInline(admin.TabularInline):
    model = ProjectToMember
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    fields = ('name', 'owner', 'created', 'modified', 'zabbix_group_id')
    readonly_fields = ('zabbix_group_id', 'created', 'modified')
    inlines = (MembershipInline,)


admin.site.register(Project, ProjectAdmin)
