# Generated by Django 4.2.1 on 2023-05-19 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Blog", "0002_rename_blocked_block"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="files",
        ),
        migrations.CreateModel(
            name="File",
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
                ("file", models.FileField(blank=True, null=True, upload_to="files/")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Blog.post"
                    ),
                ),
            ],
        ),
    ]