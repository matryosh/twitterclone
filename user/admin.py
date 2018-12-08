from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm

    form = CustomUserChangeForm

    model = CustomUser

    list_display = ('email', 'username', 'age', 'is_staff', 'first_name', 'last_name')

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email' 'first_name', 'last_name', 'age', 'bio', 'password1', 'password2', )
        }
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
