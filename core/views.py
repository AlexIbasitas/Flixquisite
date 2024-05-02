from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Movie, MyMovies, CO2, NetflixMovie
from django.contrib.auth.decorators import login_required
import re
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from django.db.models import F
import collections


# Restrict view to logged in users
@login_required(login_url='login')
def index(request):
    all_movies = Movie.objects.all()

    recently_added_movies = Movie.objects.order_by('-id')[:15]

    series = Movie.objects.filter(isSeries=True)
    movies = Movie.objects.filter(isSeries=False)


    # action_movies = Movie.objects.filter(genre='action')
    # adventure_movies = Movie.objects.filter(genre='adventure')
    # horror_movies = Movie.objects.filter(genre='horror')
    # romance_movies = Movie.objects.filter(genre='romance')
    # science_fiction_movies = Movie.objects.filter(genre='science fiction')
    # thriller_movies = Movie.objects.filter(genre='thriller')
    # fantasy_movies = Movie.objects.filter(genre='fantasy')
    # animation_movies = Movie.objects.filter(genre='animation')
    # documentary_movies = Movie.objects.filter(genre='documentary')
    # mystery_movies = Movie.objects.filter(genre='mystery')
    # comedy_movies = Movie.objects.filter(genre='comedy')

    # Add isSeries parameter to 

    # featured_movie = movies[len(movies)-1]
    featured_movie = Movie.objects.get(title="Up")

    get_movies = {
        'all_movies': all_movies,
        'featured_movie': featured_movie,
        'recently_added_movies': recently_added_movies,
        'series': series,
        'movies': movies,
    }
    return render(request, 'index.html', get_movies)

# Restrict view to logged in users
@login_required(login_url='login')
def movie(request, pk):
    movie_uu_id = pk
    movie_details = Movie.objects.get(uu_id=movie_uu_id)

    attributes = {'movie_details' : movie_details}
    
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
def remove_from_my_movies(request):
    if request.method == 'POST':
        # Get movie id
        movie_url_id = request.POST.get('movie_id')
        
        # Extract uuid pattern via regex
        uuid_regex = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        match = re.search(uuid_regex, movie_url_id)
        movie_id = match.group() if match else None
        
        # Look for movie with given ID
        movie = get_object_or_404(Movie, uu_id=movie_id)
        
        # Try to delete the movie from user's "My Movies" list
        try:
            my_movie = MyMovies.objects.get(user=request.user, movie=movie)
            my_movie.delete()
            response = {'status': 'success', 'message': 'Removed from My Movies'}
        except MyMovies.DoesNotExist:
            response = {'status': 'not_found', 'message': 'Movie not found in My Movies'}
        
        return JsonResponse(response)
    
    # Error
    response = {'status': 'error', 'message': 'Invalid Request'}
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

    movie_attributes = {
        'movies': movies,
        'movie_genre': movie_genre,
    }

    return render(request, 'genre.html', movie_attributes)


#### Netflix Wrapped ####

# 10 Insights:
# 1. Monthly Watch Time: Calculate the total watch time for each month and plot it over time to see trends in viewing habits.
# 2. Watch Time per Weekday: Analyze the average watch time for each weekday to identify patterns in viewing behavior throughout the week.
# 3. Watch Time for Different Media Types: Categorize the viewing data by media type (e.g., movies, TV shows, documentaries) and compare the watch time for each category.
# 4. Top 10 Most Watched Titles: Identify the top 10 most watched titles by total watch time and visualize them in a bar chart to see which shows or movies are the most popular.
# 5. Top 10 Most Binge-watched Shows: Calculate the binge-watching ratio for each show (i.e., the proportion of total watch time spent on consecutive episodes) and identify the top 10 shows with the highest binge-watching ratios.
# 6. Daily Viewing Patterns: Plot a histogram of the duration of viewing sessions to understand how long users typically spend watching Netflix in one sitting.
# 7. Device Usage Distribution: Analyze the distribution of watch time across different device types (e.g., smart TVs, smartphones, tablets) to see which devices are most commonly used for viewing.
# 8. Geographic Viewing Trends: Compare viewing habits across different countries or regions to identify cultural preferences or differences in content popularity.
# 9. Autoplay Engagement Analysis: Analyze the frequency and duration of autoplayed content to understand how often users continue watching after autoplay kicks in.
# 10. User Engagement Over Time: Plot the number of viewing sessions or watch time over time to track changes in user engagement with the platform.
def netflix_wrapped(request):
    watchTimeByMonth = getWatchTimeByMonth()
    watchTimeByDayOfWeek = getWatchTimeByDayOfWeek()
    top10MostWatchedTitles = getTop10MostWatchedTitles()
    
    context = {
        'watchTimeByMonth': watchTimeByMonth,
        'watchTimeByDayOfWeek': watchTimeByDayOfWeek,
        'top10MostWatchedTitles': top10MostWatchedTitles,
    }
    return render(request, 'netflix_wrapped.html', context)



def getTop10MostWatchedTitles():
    netflix_viewing_queryset = NetflixMovie.objects.all()  

    # Aggregate watch time for each title
    title_watch_time = collections.defaultdict(int)

    for viewing in netflix_viewing_queryset:
        title = viewing.title
        
        # Calculate the duration in minutes
        duration_minutes = viewing.duration.total_seconds() / 60
        
        # Add the duration to the corresponding title in the dictionary
        title_watch_time[title] += duration_minutes

    # Sort titles by watch time and select the top 10
    top_10_titles = sorted(title_watch_time.items(), key=lambda x: x[1], reverse=True)[:10]

    # Extract titles and watch times for plotting
    titles = [title for title, _ in top_10_titles]
    watch_times = [watch_time for _, watch_time in top_10_titles]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=titles,
        y=watch_times,
        marker_color='rgb(255, 0, 0)'
    ))

    fig.update_layout(
        title='Top 10 Most Watched Titles',
        xaxis=dict(title='Title'),
        yaxis=dict(title='Total Watch Time (minutes)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    chart = fig.to_html()   
    return chart

def getWatchTimeByDayOfWeek():
    netflix_viewing_queryset = NetflixMovie.objects.all()  

    # Extract data for watch time by weekday
    weekday_watch_time = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}

    for viewing in netflix_viewing_queryset:
        # Extract weekday from the viewing start time
        weekday = viewing.start_time.strftime('%A')
        
        # Calculate the duration in minutes
        duration_minutes = viewing.duration.total_seconds() / 60
        
        # Add the duration to the corresponding weekday in the dictionary
        weekday_watch_time[weekday] += duration_minutes

    # Extract weekdays and watch times for plotting
    weekdays = list(weekday_watch_time.keys())
    watch_times = list(weekday_watch_time.values())

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=weekdays,
        y=watch_times,
        marker_color='rgb(255, 0, 0)'  # Red color
    ))

    fig.update_layout(
        title='Watch Time by Weekday',
        xaxis=dict(title='Weekday'),
        yaxis=dict(title='Total Watch Time (minutes)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    chart = fig.to_html()
    return chart



def getWatchTimeByMonth():
    netflix_viewing_queryset = NetflixMovie.objects.all()  

    monthly_watch_time = {}

    for viewing in netflix_viewing_queryset:
        month_year = viewing.start_time.strftime('%Y-%m')
        
        duration_minutes = viewing.duration.total_seconds() / 60
        
        if month_year in monthly_watch_time:
            monthly_watch_time[month_year] += duration_minutes
        else:
            monthly_watch_time[month_year] = duration_minutes

    sorted_monthly_watch_time = dict(sorted(monthly_watch_time.items()))

    months = []
    watch_times = []

    for month, watch_time in sorted_monthly_watch_time.items():
        months.append(month)
        watch_times.append(watch_time)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months,
        y=watch_times,
        mode='lines+markers',
        marker=dict(color='rgb(255, 0, 0)'),  
        line=dict(width=2)
    ))

    fig.update_layout(
        title='Total Watch Time per Month',
        xaxis=dict(title='Month'),
        yaxis=dict(title='Total Watch Time (minutes)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    chart = fig.to_html()
    return chart



