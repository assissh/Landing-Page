# Generated by Django 2.0.3 on 2018-03-24 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Educationinfo_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Educationinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Educationinfo_Course', models.CharField(max_length=100)),
                ('Educationinfo_Course_Detail', models.CharField(max_length=100)),
                ('Educationinfo_Institute', models.CharField(max_length=100)),
                ('Educationinfo_Passing_Year', models.CharField(max_length=100)),
                ('Educationinfo_Modified_Date', models.DateField()),
                ('Educationinfo_Created_Time', models.DateField()),
                ('Educationinfo_Message', models.CharField(max_length=280)),
                ('Educationinfo_Creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educationinfos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Educationinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsEducationinfo', to='EducationInfos.Educationinfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Educationinfo_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssEducationinfo', to=settings.AUTH_USER_MODEL),
        ),
    ]
