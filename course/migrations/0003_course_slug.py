# Generated by Django 4.1.4 on 2022-12-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_codetest_description_alter_course_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]