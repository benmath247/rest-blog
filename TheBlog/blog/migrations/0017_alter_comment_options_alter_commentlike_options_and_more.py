# Generated by Django 4.0 on 2021-12-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_postreaction_reaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='commentlike',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='postreaction',
            options={'ordering': ['-created_on']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='date_added',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='commentlike',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='like',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='postreaction',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
