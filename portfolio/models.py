from django.db import models


class Theme(models.Model):
    primary_color = models.CharField(max_length=7)
    secondary_color = models.CharField(max_length=7)
    favicon_image = models.ImageField(upload_to="images/", blank=True)

    class Meta:
        # meta data attribute for the display in the admin panel
        verbose_name_plural = "Theme"

    def save(self, *args, **kwargs):
        # self.pk doesn't exist for new instances (allows editting)
        if not self.pk and Theme.objects.exists():
            raise ValueError("Only one instance of Theme can be created.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return "Portfolio Theme"


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/user_profile/")
    email = models.EmailField()
    resume_url = models.URLField()
    social = models.ManyToManyField("Social", blank=True)

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
    category = models.CharField(max_length=2, choices=SKILL_CATEGORIES)
    level = models.CharField(max_length=1, choices=SKILL_LEVELS)

    def __str__(self):
        return self.name
