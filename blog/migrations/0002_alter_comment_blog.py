# Generated by Django 4.1 on 2023-06-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="blog",
            field=models.IntegerField(blank=True),
        ),
    ]
