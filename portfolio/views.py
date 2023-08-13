from django.views import View
from django.shortcuts import render

from portfolio.models import Project, Skill, UserProfile


class HomePageView(View):
    def get(self, request):
        user_profile = UserProfile.objects.first()
        projects = Project.objects.all()
        skills = Skill.objects.all()

        context = {
            "user_profile": user_profile,
            "projects": projects,
            "skills": skills,
        }

        return render(request, "portfolio.html", context)
