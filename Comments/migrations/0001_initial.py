# Generated by Django 2.0.3 on 2018-04-04 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comments_Comments', models.CharField(max_length=150)),
                ('Comments_Comment_Created_On', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comments_Comment', models.CharField(max_length=100, unique=True)),
                ('Comments_Helpfull', models.CharField(max_length=100)),
                ('Comments_Modified_Date', models.DateTimeField(auto_now_add=True)),
                ('Comments_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_Comment', to='Comments.Comments'),
        ),
    ]
