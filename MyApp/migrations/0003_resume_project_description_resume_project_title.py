# Generated by Django 4.2.2 on 2023-10-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_resume_brief_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='project_description',
            field=models.TextField(default='YourDefaultHere', max_length=1000),
        ),
        migrations.AddField(
            model_name='resume',
            name='project_title',
            field=models.CharField(default='YourDefaultHere', max_length=100),
        ),
    ]
