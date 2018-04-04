# Generated by Django 2.0.2 on 2018-04-04 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location_subcategory', '0002_auto_20180404_1258'),
        ('Location_Category', '0002_auto_20180404_1258'),
        ('Location', '0003_auto_20180404_0426'),
        ('Search', '0002_auto_20180404_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='Search_CATEGORY',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Searchcategory', to='Location_Category.Location_Category'),
        ),
        migrations.AddField(
            model_name='search',
            name='Search_Location_List',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Searchlocationlist', to='Location.Location'),
        ),
        migrations.AddField(
            model_name='search',
            name='Search_Sub_Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SearchSubCategory', to='location_subcategory.LocationSubCategory'),
        ),
    ]
