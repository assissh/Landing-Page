# Generated by Django 2.0.3 on 2018-04-04 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Costume_Comment', models.CharField(max_length=150)),
                ('Costume_Comment_Created_On', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Costume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Costume_Color', models.CharField(max_length=100)),
                ('Costume_Category', models.CharField(max_length=100)),
                ('Costume_Style', models.CharField(max_length=100)),
                ('Costume_Description', models.CharField(max_length=100)),
                ('Costume_Type', models.CharField(max_length=100)),
                ('Costume_Modification_Allowed', models.BooleanField()),
                ('Costume_Trend_Year', models.DateField()),
                ('Costume_Weekly_Rent', models.IntegerField()),
                ('Costume_Modified_Date', models.DateField(auto_now_add=True)),
                ('Costume_Created_Date', models.DateField(auto_now_add=True)),
                ('Costume_Creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Costumes', to=settings.AUTH_USER_MODEL)),
                ('Costume_Image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CostumesImage', to='Images.Image')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Costume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CostumeComment', to='Costumes.Costume'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Costume_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CostumeComments', to=settings.AUTH_USER_MODEL),
        ),
    ]
