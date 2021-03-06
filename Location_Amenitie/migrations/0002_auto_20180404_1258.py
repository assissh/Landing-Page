# Generated by Django 2.0.3 on 2018-04-04 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Location_Amenitie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location_amenitie',
            name='Location_Amenitie_Creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locatonamenities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='Location_Amenitie_Comment_Location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location_Amenitie.Location_Amenitie'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Location_Amenitie_Location_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentLocation_Amenitie', to=settings.AUTH_USER_MODEL),
        ),
    ]
