from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    list_display = ['id', 'firstname','lastname']
    search_fields = ('email',)
    ordering= ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstname','lastname', 'password1', 'password2','is_active',),
        }),
    )


admin.site.register(User, UserAdmin)