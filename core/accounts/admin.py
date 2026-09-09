from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active", "is_verified")
    list_filter = ("email", "is_staff", "is_active", "is_verified")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions", "is_verified")}),
        ("Important date", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        ('Permissions', {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff", "is_verified",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    

admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)