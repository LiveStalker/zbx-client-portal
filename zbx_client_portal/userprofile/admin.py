from django.contrib import admin
from .forms import UserProfileForm
from .models import UserProfile, UserLanguage


class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    fields = ('user', 'language', 'timezone', 'zabbix_user_id', 'created', 'modified')
    readonly_fields = ('zabbix_user_id', 'created', 'modified')


class UserLanguageAdmin(admin.ModelAdmin):
    fields = ('language', 'language_code')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserLanguage, UserLanguageAdmin)
