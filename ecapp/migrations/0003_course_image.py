# Generated by Django 4.1.2 on 2022-10-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecapp', '0002_course_cdescription_course_cobjectives_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
