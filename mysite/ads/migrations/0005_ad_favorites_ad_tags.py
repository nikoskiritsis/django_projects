# Generated by Django 4.2.3 on 2023-10-17 10:26

from django.conf import settings
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0005_auto_20220424_2025"),
        ("ads", "0004_fav"),
    ]

    operations = [
        migrations.AddField(
            model_name="ad",
            name="favorites",
            field=models.ManyToManyField(
                related_name="favorite_ads",
                through="ads.Fav",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="ad",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
