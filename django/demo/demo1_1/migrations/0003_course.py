# Generated by Django 4.2.1 on 2023-08-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demo1_1", "0002_remove_userinfo_id_userinfo_shortlisted_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("course_name", models.CharField(max_length=100)),
                ("course_id", models.CharField(max_length=10, unique=True)),
                ("enroll", models.CharField(default="register now", max_length=20)),
            ],
        ),
    ]
