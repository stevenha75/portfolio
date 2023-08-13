from django.views import View
from django.shortcuts import render

from portfolio.models import Project, Skill, Theme, UserProfile


class HomePageView(View):
    def get(self, request):
        theme = Theme.objects.first()  # TODO: This might not be too useful?
        user_profile = UserProfile.objects.first()
        projects = Project.objects.all()
        skills = Skill.objects.all()

        context = {
            "theme": theme,
            "user_profile": user_profile,
            "projects": projects,
            "skills": skills,
        }

        return render(request, "home.html", context)
