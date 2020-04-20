
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User as MainUser
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','gender','date_of_birth','profile_image')}),
        (_('Skills'), {'fields': ('badges',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'username', 'password1', 'password2')
            }
        ),
    )
    # list_display = ('email', 'username', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email','username',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(MainUser)
admin.site.register(User, UserAdmin)
