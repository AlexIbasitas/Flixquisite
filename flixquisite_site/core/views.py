from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Movie, MyMovies
from django.contrib.auth.decorators import login_required
import re
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

@login_required(login_url='login')
def index(request):
    movies = Movie.objects.all()
    get_movies = {'movies': movies}
    return render(request, 'index.html', get_movies)

# Restrict view to logged in users
@login_required(login_url='login')
def movie(request, pk):
    movie_uu_id = pk
    movie_attributes = Movie.objects.get(uu_id=movie_uu_id)

    attributes = {'movie_attributes' : movie_attributes}
    print("Getting Movie")
    
    return render(request, 'movie.html', attributes)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        auth_user = auth.authenticate(username=username, password=password)

        # Check existence for the user in the DB
        if auth_user:
            auth.login(request, auth_user)
            return redirect('/')
        
        messages.info(request, 'Invalid credentials')
        return redirect('login')
    
    return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        # Gather signup attributes sent from User in the signup form
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']

        # Check user has correctly inputted both passswords
        if password != repeat_password:
            # send message back to signup.html
            messages.info(request, 'Passwords do not match, please try again.')
            # send user back to the signup page
            return redirect('signup')

        # Check DB by filtering User table and seeing if the email received from the POST method matches any email in the User table
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email has already been used, please try again.')
            # send user back to the signup page
            return redirect('signup')
        # Check that username has not already been taken
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username has already been taken, please try again.')
            # send user back to the signup page
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            auth_user = auth.authenticate(username=username, password=password)
            auth.login(request, auth_user)
            return redirect('/')
    
    return render(request, 'signup.html')

@login_required(login_url='login')
def my_movies(request):
    # Get all movies from the user's movie list
    movie_list = MyMovies.objects.filter(user=request.user)
    user_movie_list = [movie.movie for movie in movie_list]
    movie_attributes = {'movies' : user_movie_list}
    return render(request, 'my_movies.html', movie_attributes)

@login_required(login_url='login')
def add_to_my_movies(request):
    if request.method == 'POST':
        # Get id
        movie_url_id = request.POST.get('movie_id')
        
        # Extract uuid pattern via regex
        uuid_regex = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        match = re.search(uuid_regex, movie_url_id)
        movie_id = match.group() if match else None
        
        # Look for id same as uuid
        movie = get_object_or_404(Movie, uu_id=movie_id)

        # If user has already added movie to My Movies, then tell user that movie is already in list
        # If movie is not in My Movies, add to My Movies and let user know it has been added.
        _, created = MyMovies.objects.get_or_create(user=request.user, movie=movie)
        
        if created:
            response = {'status' : 'success', 'message': 'Added to My Movies'}
        else:
            response = {'status' : 'added', 'message': 'Movie already in My Movies'}
        
        return JsonResponse(response)
    
    # Error
    response = {'status' : 'error', 'message': 'Invalid Request'}
    return JsonResponse(response, status=400)


@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']

        # Filter all objects in movies that contain the search term in its title
        movies = Movie.objects.filter(title__icontains=search_term)

        movie_attributes = {
            'movies' : movies,
            'search_term': search_term,
        }

        return render(request, 'search.html', movie_attributes)
    
    return redirect('/')
    
@login_required(login_url='login')
def genre(request, pk):
    movie_genre = pk
    movies = Movie.objects.filter(genre=movie_genre)
    return render(request, 'genre.html')

