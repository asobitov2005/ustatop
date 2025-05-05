from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from booking.models import Service, Booking, Rating


from .models import User
admin.site.register(User)

# User = get_user_model()

# 
# @admin.register(User)
# class CustomUserAdmin(BaseUserAdmin):
#     list_display = ("id", "username", "email", "role", "is_active", "is_staff")
#     list_filter = ("role", "is_active", "is_staff", "is_superuser")
#     search_fields = ("username", "email")
#     ordering = ("id",)
# 
#     fieldsets = (
#         (None, {"fields": ("username", "email", "password")}),
#         ("Permissions", {"fields": ("role", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
#         ("Important dates", {"fields": ("last_login", "date_joined")}),
#     )
# 
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": ("username", "email", "role", "password1", "password2", "is_active", "is_staff", "is_superuser")
#         }),
#     )
# 
# 
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ("id", "type", "provider", "price")
#     list_filter = ("type",)
#     search_fields = ("type", "description", "provider__username")
#     autocomplete_fields = ("provider",)
#     ordering = ("id",)
# 
# 
# class RatingInline(admin.TabularInline):
#     model = Rating
#     extra = 0
#     readonly_fields = ("user", "rating", "review", "created_at")
#     can_delete = False
# 
# 
# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ("id", "client", "service", "scheduled_date", "status")
#     list_filter = ("status", "scheduled_date")
#     search_fields = ("client__username", "service__type")
#     autocomplete_fields = ("client", "service")
#     ordering = ("scheduled_date",)
#     date_hierarchy = "scheduled_date"
#     inlines = [RatingInline]
# 
# 
# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ("id", "booking", "user", "rating", "created_at")
#     list_filter = ("rating", "created_at")
#     search_fields = ("user__username", "booking__id")
#     autocomplete_fields = ("booking", "user")
#     ordering = ("-created_at",)

