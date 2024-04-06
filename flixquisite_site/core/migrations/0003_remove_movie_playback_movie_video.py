# Generated by Django 5.0.4 on 2024-04-06 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_movie_date_movie_description_movie_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='playback',
        ),
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(default='media/images/default_image.png', upload_to='movie/'),
        ),
    ]
