# Generated by Django 2.0.2 on 2018-04-04 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileProjects', '0001_initial'),
        ('Video', '0001_initial'),
        ('Ratings', '0002_auto_20180404_1258'),
        ('Location_Amenitie', '0002_auto_20180404_1258'),
        ('Comments', '0002_comment_comments_comment_author'),
        ('image', '0001_initial'),
        ('Location_Category', '0002_auto_20180404_1258'),
        ('Location', '0002_auto_20180404_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='Location_Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='Location_Category.Location_Category'),
        ),
        migrations.AddField(
            model_name='location',
            name='Location_Comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='Comments.Comments'),
        ),
        migrations.AddField(
            model_name='location',
            name='Location_Images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='image.Image'),
        ),
        migrations.AddField(
            model_name='location',
            name='Location_Profile_Project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='ProfileProjects.ProfileProjects'),
        ),
        migrations.AddField(
            model_name='location',
            name='Location_Rating',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='Ratings.Rating'),
        ),
        migrations.AddField(
            model_name='location',
            name='Location_Shooting_Aminities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LocationAmenities', to='Location_Amenitie.Location_Amenitie'),
        ),
        migrations.AddField(
            model_name='location',
            name='Location_Video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='Video.Video'),
        ),
    ]
