# Generated by Django 3.2.9 on 2021-12-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
    ]
