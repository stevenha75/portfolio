from django.db import models


class UserProfile(models.Model):
    image = models.ImageField(upload_to="user_profile/", blank=True)
    name = models.CharField(max_length=100)
    resume_url = models.URLField()
    social = models.ManyToManyField("Social")

    def __str__(self):
        return self.name


class Social(models.Model):
    platform = models.CharField(max_length=100)
    profile_url = models.URLField()
    icon_class = models.CharField(max_length=50)

    def __str__(self):
        return self.platform


class Project(models.Model):
    name = models.CharField(max_length=255)
    skills = models.ManyToManyField("Skill")
    url = models.URLField()
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    SKILL_CATEGORIES = (
        ("TT", "Tools / Technologies"),
        ("LF", "Languages / Frameworks"),
    )

    SKILL_LEVELS = (
        ("P", "Proficient"),
        ("F", "Familiar"),
    )

    name = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=50)
    category = models.CharField(max_length=2, choices=SKILL_CATEGORIES)
    level = models.CharField(max_length=1, choices=SKILL_LEVELS)

    def __str__(self):
        return self.name
