# Generated by Django 4.0 on 2021-12-26 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_post_attachment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="attachment",
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
    ]
