# Generated by Django 4.1.4 on 2023-01-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_remove_coursetask_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetask',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]