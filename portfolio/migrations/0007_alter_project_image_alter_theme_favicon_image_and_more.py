# Generated by Django 4.2.4 on 2023-08-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_theme_alter_project_image_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/projects/'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='favicon_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='images/user_profile/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social',
            field=models.ManyToManyField(blank=True, to='portfolio.social'),
        ),
    ]
