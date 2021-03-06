# Generated by Django 2.0.3 on 2018-04-04 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContactMessages_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContactMessages_Address', models.CharField(max_length=100, unique=True)),
                ('ContactMessages_Camera_Model', models.CharField(max_length=100)),
                ('ContactMessages_City_State_Country', models.CharField(max_length=100)),
                ('ContactMessages_Company_Name', models.CharField(max_length=100)),
                ('ContactMessages_Email', models.EmailField(max_length=100)),
                ('ContactMessages_From_Page', models.CharField(max_length=100)),
                ('ContactMessages_From_Resource', models.CharField(max_length=100)),
                ('ContactMessages_Full_Name', models.CharField(max_length=100)),
                ('ContactMessages_Message', models.CharField(max_length=100)),
                ('ContactMessages_Phone_Number', models.IntegerField(default=-1)),
                ('ContactMessages_Profile', models.CharField(max_length=100)),
                ('ContactMessages_Modified_Date', models.DateTimeField(auto_now_add=True)),
                ('ContactMessages_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_ContactMessages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment_ContactMessages', to='ContactMessages.ContactMessages'),
        ),
    ]
