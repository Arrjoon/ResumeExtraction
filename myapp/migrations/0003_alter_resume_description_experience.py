# Generated by Django 5.0.6 on 2024-07-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_job_description_resume_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_description',
            name='experience',
            field=models.CharField(max_length=20, null=True),
        ),
    ]