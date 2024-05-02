from django.db import models
import uuid
import datetime
from django.conf import settings


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

    title = models.CharField(max_length=255)
    description = models.TextField(default='No description available.')
    date = models.DateField(("Date"), default=datetime.date.today)
    genre = models.CharField(max_length=50, default='No genre available', choices=GENRES)
    length = models.PositiveBigIntegerField(default=0)
    image_carousel_card = models.ImageField(upload_to='images/', default='images/default_image.png')
    image_feature_cover = models.FileField(upload_to='images/', default='images/default_image.png')
    video = models.FileField(upload_to='movie/', default='movie/65aaa30f-af07-4968-a1b0-c107bc902b90.mp4')
    isSeries = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class MyMovies(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class CO2(models.Model):
    date = models.DateField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',)


class NetflixMovie(models.Model):
    # Profile Name,Start Time,Duration,Attributes,Title,Supplemental Video Type,Device Type,Bookmark,Latest Bookmark,Country
    profile_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    duration = models.DurationField()
    attributes = models.TextField()
    title = models.CharField(max_length=255)
    supplemental_video_type = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    bookmark = models.DurationField()
    latest_bookmark = models.DurationField()
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ('start_time',)
