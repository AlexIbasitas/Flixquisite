from django.db import models
import uuid
# Create your models here.
class Movie(models.Model):
    def __init__(self):
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
            ('mystery', 'Mystery')
        ]

        id = models.UUIDField(default=uuid.uuid4)

        title = models.CharField(max_length=255)
        description = models.TextField()
        date = models.DateField()
        genre = models.CharField(max_length=50, choices=GENRES)
        length = models.PositiveBigIntegerField()

        image_carousel_card = models.ImageField(upload_to='movie_images/')
        image_feature_cover = models.FileField(upload_to='movie_images/')
        playback = models.FileField(upload_to='movie_videos/')

    def __str__(self):
        return self.title