# Generated by Django 4.2.1 on 2023-06-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='off_price',
            field=models.IntegerField(default=0),
        ),
    ]
