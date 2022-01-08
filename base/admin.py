from django.contrib import admin
from django.contrib.auth.models import User
from .models import Notice, Feed, Feed_Type, Team_member, Team_Type

# Register your models here.

@admin.register(Notice)
class PostAdmin(admin.ModelAdmin):
    list_display = (['title'])

@admin.register(Team_Type)
class PostAdmin(admin.ModelAdmin):
    list_display = (['category'])

@admin.register(Team_member)
class PostAdmin(admin.ModelAdmin):
    list_display = (['designation'])

@admin.register(Feed_Type)
class PostAdmin(admin.ModelAdmin):
    list_display = (['category'])

@admin.register(Feed)
class PostAdmin(admin.ModelAdmin):
    list_display = (['title','category'])
    list_filter =(['category'])
