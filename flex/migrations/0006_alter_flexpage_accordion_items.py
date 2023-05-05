# Generated by Django 4.1.8 on 2023-05-03 10:32

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("flex", "0005_flexpage_accordion_items"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flexpage",
            name="accordion_items",
            field=wagtail.fields.StreamField(
                [
                    (
                        "accordion_item",
                        wagtail.blocks.StructBlock(
                            [
                                ("issue", wagtail.blocks.CharBlock(required=True)),
                                ("fix", wagtail.blocks.RichTextBlock(required=True)),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=None,
            ),
        ),
    ]
