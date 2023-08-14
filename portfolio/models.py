# TODO: Figure out a way to handle image names (maybe UUID?)
from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/user_profile/")
    email = models.EmailField()
    resume_url = models.URLField()
    social = models.ManyToManyField("Social", blank=True)
    favicon_image = models.ImageField(upload_to="images/", blank=True)

    class Meta:
        verbose_name_plural = "User Profile"

    def save(self, *args, **kwargs):
        if not self.pk and UserProfile.objects.exists():
            raise ValueError("Only one instance of UserProfile can be created.")
        return super().save(*args, **kwargs)

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
    image = models.ImageField(upload_to="images/projects/")

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
    url = models.URLField(blank=True)
    category = models.CharField(max_length=2, choices=SKILL_CATEGORIES)
    level = models.CharField(max_length=1, choices=SKILL_LEVELS)

    def __str__(self):
        return self.name
