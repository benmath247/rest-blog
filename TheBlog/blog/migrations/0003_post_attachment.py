# Generated by Django 4.0 on 2021-12-26 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="attachment",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]
