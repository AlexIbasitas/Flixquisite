from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('movie/<str:pk>/', views.movie, name='movie'),
    path('my-movies', views.my_movies, name='my-movies'),
    path('add-to-my-movies', views.add_to_my_movies, name='add-to-my-movies'),
]