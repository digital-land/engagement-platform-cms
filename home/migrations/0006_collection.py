# Generated by Django 4.1.9 on 2023-06-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_alter_homepage_options_homepage_banner_cta_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="collection",
            fields=[
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("description", models.CharField(max_length=500)),
                ("specification_URL", models.URLField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "collection",
                "verbose_name_plural": "collections",
            },
        ),
    ]
