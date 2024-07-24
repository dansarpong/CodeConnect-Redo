from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff',)
    list_filter = ('email', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'date_joined',)}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff')}
        ),
    )
    search_fields = ('email', 'username',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
