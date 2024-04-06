from django.db import models
import uuid
import datetime

# Create your models here.
class Movie(models.Model):
    GENRES = [
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science_fiction', 'Science Fiction'),
        ('thriller', 'Thriller'),
        ('fantasy', 'Fantasy'),
        ('animation', 'Animation'),
        ('documentary', 'Documentary'),
        ('mystery', 'Mystery'),
        ('comedy', 'Comedy')
    ]

    uu_id = models.UUIDField(default=uuid.uuid4)

    title = models.CharField(max_length=255, default='No title')
    description = models.TextField(default='No description available.')
    date = models.DateField(("Date"), default=datetime.date.today)
    genre = models.CharField(max_length=50, default='No genre available', choices=GENRES)
    length = models.PositiveBigIntegerField(default=0)

    image_carousel_card = models.ImageField(upload_to='images/', default='media/images/default_image.png')
    image_feature_cover = models.FileField(upload_to='images/', default='media/images/default_image.png')
    playback = models.FileField(upload_to='playback/', default='media/images/default_image.png')



    def __str__(self):
        return self.title