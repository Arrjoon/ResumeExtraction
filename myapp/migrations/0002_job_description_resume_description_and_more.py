# Generated by Django 5.0.6 on 2024-07-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(max_length=50)),
                ('company_description', models.TextField()),
                ('role_description', models.TextField()),
                ('qualification', models.TextField(null=True)),
                ('degree', models.CharField(max_length=100, null=True)),
                ('experience', models.IntegerField()),
                ('skills', models.TextField(help_text='Comma-separated list of skills')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('company_working_at', models.CharField(max_length=100, null=True)),
                ('degree', models.CharField(max_length=100, null=True)),
                ('college_name', models.CharField(max_length=100, null=True)),
                ('graduation_year', models.CharField(max_length=20, null=True)),
                ('experience', models.IntegerField(null=True)),
                ('university', models.CharField(max_length=25, null=True)),
                ('skills', models.TextField(help_text='Comma-separated list of skills')),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='job_description',
        ),
        migrations.DeleteModel(
            name='JobDescription',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
