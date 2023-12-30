from django.contrib import admin
from Blog.models import User, Posts


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "password","profile")


class PostsAdmin(admin.ModelAdmin):
    list_display = ("writen_by", "description","image", "created_at")


admin.site.register(User, UserAdmin)
admin.site.register(Posts, PostsAdmin)
