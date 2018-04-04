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
                ('Help_Center_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='HelpCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help_Center_Help_Name', models.CharField(max_length=100)),
                ('Help_Center_Help_Id', models.IntegerField()),
                ('Help_Center_Modified_Date', models.DateField(auto_now_add=True)),
                ('Help_Center_Created_Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
