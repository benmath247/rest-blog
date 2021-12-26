# Generated by Django 4.0 on 2021-12-26 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211223_2053'),
        ('blog', '0007_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reactions', models.CharField(choices=[('LIKE', 'Like'), ('LOVE', 'Love'), ('SAD', 'Sad'), ('ANGRY', 'Angry'), ('FIRE', 'Fire'), ('CLAP', 'Clap')], default=None, max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_reactions', to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reactions', to='accounts.user')),
            ],
        ),
    ]