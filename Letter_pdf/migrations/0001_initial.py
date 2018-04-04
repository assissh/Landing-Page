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
                ('Letter_pdf_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Letter_pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Letter_pdf_Addressing_Officer', models.CharField(max_length=100)),
                ('Letter_pdf_Project', models.CharField(max_length=100)),
                ('Letter_pdf_Modified_Date', models.DateField(auto_now_add=True)),
                ('Letter_pdf_Created_Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
