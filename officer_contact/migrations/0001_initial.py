# Generated by Django 2.0.3 on 2018-04-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officer_contact_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='OfficerContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OfficerContact_CONTACT_NUMBER', models.CharField(max_length=200)),
                ('OfficerContact_DEPARTMENT', models.CharField(max_length=200)),
                ('OfficerContact_DESIGNATIONS', models.CharField(max_length=200)),
                ('OfficerContact_E_Mail', models.EmailField(max_length=200)),
                ('OfficerContact_Name', models.CharField(max_length=200)),
                ('OfficerContact_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
