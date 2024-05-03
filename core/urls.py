from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('movie/<str:pk>/', views.movie, name='movie'),
    path('genre/<str:pk>/', views.genre, name='genre'),
    path('my-movies', views.my_movies, name='my-movies'),
    path('add-to-my-movies', views.add_to_my_movies, name='add-to-my-movies'),
    path('remove-from-my-movies', views.remove_from_my_movies, name='remove-from-my-movies'),
    path('search', views.search, name='search'),

    path('netflix-wrapped', views.netflix_wrapped, name='netflix-wrapped'),

    path('netflix-wrapped-landing-page', views.netflix_wrapped_landing_page, name='netflix-wrapped-landing-page'),

]