from django.contrib import admin

from .models import Profile, Image



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = 'pk', 'fullName', 'email', 'phone'
    list_display_links = 'pk', 'fullName', 'email'
    search_fields = 'fullName', 'email'

    fieldsets = [
        (None, {
            'fields': ('fullName', 'email', 'phone', 'user', 'avatar')
        }),
    ]


@admin.register(Image)
class AvatarAdmin(admin.ModelAdmin):
    list_display = 'pk', 'alt'
    list_display_links = 'pk', 'alt'
    search_fields = 'alt',
    fieldsets = [
        (None, {
            'fields': ('src', 'alt')
        })
    ]