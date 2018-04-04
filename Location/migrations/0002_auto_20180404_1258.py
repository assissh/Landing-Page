# Generated by Django 2.0.3 on 2018-04-04 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='Location_Authorities_Involved',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locationss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='location',
            name='Location_Creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crlocations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location.Location'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Location_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentlocation', to=settings.AUTH_USER_MODEL),
        ),
    ]