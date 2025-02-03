# Generated by Django 5.1.5 on 2025-02-03 16:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0004_alter_question_solution_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="solution_image",
            field=cloudinary.models.CloudinaryField(
                blank=True,
                default="https://res.cloudinary.com/dsvh54olg/image/upload/v1738599609/torn-style-coming-soon-promo-template-social-media-post_1017-55783_oqolic.avif",
                max_length=255,
                null=True,
                verbose_name="solutions/",
            ),
        ),
    ]
