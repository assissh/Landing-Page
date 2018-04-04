# Generated by Django 2.0.3 on 2018-04-04 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ChildArtist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Child_Artist_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childartists', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Child_Artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='ChildArtist.ChildArtist'),
        ),
    ]
