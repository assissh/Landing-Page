# Generated by Django 2.0.3 on 2018-04-02 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceSubcatagory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Comment_ServiceSubcatagory',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='ServiceSubcatagory_Comment_Author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='ServiceSubcatagory',
        ),
    ]