# Generated by Django 2.0.3 on 2018-04-04 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_Comment', models.CharField(max_length=150)),
                ('Image_Comment_Created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_My_Image', models.ImageField(upload_to='')),
                ('Image_Owned_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagecommentss', to='Images.Image'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Image_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagecomments', to=settings.AUTH_USER_MODEL),
        ),
    ]
