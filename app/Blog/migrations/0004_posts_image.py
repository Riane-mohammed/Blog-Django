# Generated by Django 5.0 on 2023-12-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Blog", "0003_posts_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="posts",
            name="image",
            field=models.ImageField(default="", upload_to="", verbose_name="Post Pic"),
            preserve_default=False,
        ),
    ]
