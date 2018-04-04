# Generated by Django 2.0.3 on 2018-04-04 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location_pitch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationpitch',
            name='LocationPitch_By_User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_pitchs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='locationpitch',
            name='location_pitch_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_location_pitch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_pitch.LocationPitch'),
        ),
    ]