# Generated by Django 4.1.4 on 2023-01-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_remove_coursereview_stars_coursereview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursereview',
            name='rating',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
