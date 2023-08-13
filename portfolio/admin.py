from django.contrib import admin

from portfolio.models import Project, Skill, Social, Theme, UserProfile


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    ...


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    ...


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    ...


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ...


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    ...
