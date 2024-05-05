from django.contrib import admin
from .models import Movie, MyMovies, NetflixMovie

# Register your models here.
admin.site.register(Movie)
admin.site.register(MyMovies)
admin.site.register(NetflixMovie)