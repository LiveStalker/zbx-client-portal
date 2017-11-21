from django.contrib import admin
from .forms import UserProfileForm
from .models import UserProfile, UserLanguage, BadUsername


class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    fields = ('user', 'language', 'timezone', 'zabbix_user_id', 'created', 'modified')
    readonly_fields = ('zabbix_user_id', 'created', 'modified')


class UserLanguageAdmin(admin.ModelAdmin):
    fields = ('language', 'language_code')


class BadUsernameAdmin(admin.ModelAdmin):
    fields = ('username',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserLanguage, UserLanguageAdmin)
admin.site.register(BadUsername, BadUsernameAdmin)
