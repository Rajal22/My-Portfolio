from django.contrib import admin
from .models import Project, Skill, Message


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "order")
    list_editable = ("order",)
    search_fields = ("title", "tech_stack")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "is_read")
    list_filter = ("is_read",)
    list_editable = ("is_read",)
    readonly_fields = ("name", "email", "content", "created_at")
