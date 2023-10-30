from django.contrib import admin

from users.models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    fields = ('username', 'password', 'token',)
    readonly_fields = ('token', )

