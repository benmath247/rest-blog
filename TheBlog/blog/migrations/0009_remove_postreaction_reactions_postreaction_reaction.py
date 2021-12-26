# Generated by Django 4.0 on 2021-12-26 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_postreaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postreaction',
            name='reactions',
        ),
        migrations.AddField(
            model_name='postreaction',
            name='reaction',
            field=models.CharField(choices=[('LIKE', 'Like'), ('LOVE', 'Love'), ('SAD', 'Sad'), ('ANGRY', 'Angry'), ('FIRE', 'Fire'), ('CLAP', 'Clap')], max_length=10, null=True),
        ),
    ]