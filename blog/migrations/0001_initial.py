# Generated by Django 4.1 on 2023-06-01 12:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("topic", models.CharField(default="python", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, default="name", max_length=80)),
                (
                    "email",
                    models.EmailField(blank=True, default="email", max_length=254),
                ),
                (
                    "your_comment",
                    models.CharField(
                        blank=True, default="your comment", max_length=500
                    ),
                ),
                ("created_on", models.DateTimeField(default=datetime.datetime.now)),
                ("active", models.BooleanField(default=False)),
                ("blog", models.IntegerField(blank=True, default=1)),
            ],
            options={
                "ordering": ["created_on"],
            },
        ),
        migrations.CreateModel(
            name="Writer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("writer_name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("blog_title", models.CharField(default="Title", max_length=100)),
                ("blog_text", models.TextField(default="My Blog", max_length=10000)),
                ("blog_image", models.ImageField(upload_to="blog/")),
                ("blog_date_time", models.DateTimeField(default=datetime.datetime.now)),
                (
                    "blog_category",
                    models.OneToOneField(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category",
                        to="blog.category",
                    ),
                ),
                (
                    "writer_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="writer",
                        to="blog.writer",
                    ),
                ),
            ],
        ),
    ]
