from django.contrib import admin
from .forms import UserProfileForm
from .models import UserProfile, UserLanguage


class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    fields = ('user', 'language', 'timezone')


class UserLanguageAdmin(admin.ModelAdmin):
    fields = ('language',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserLanguage, UserLanguageAdmin)
