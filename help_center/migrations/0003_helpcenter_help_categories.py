# Generated by Django 2.0.2 on 2018-04-04 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('help_category', '0003_help_category_help_subcategory'),
        ('help_center', '0002_auto_20180404_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpcenter',
            name='Help_Categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helpcategories', to='help_category.Help_Category'),
        ),
    ]