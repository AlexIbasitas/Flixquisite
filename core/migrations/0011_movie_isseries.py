# Generated by Django 4.0.3 on 2024-05-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_netflixmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='isSeries',
            field=models.BooleanField(default=False),
        ),
    ]
