from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Movie, MyMovies, NetflixMovie, UserMovie
from django.contrib.auth.decorators import login_required
import re
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import plotly.graph_objs as go
import collections
from datetime import time, timedelta, datetime
from django.core.cache import cache
from django.shortcuts import render
from django.utils import timezone
from .forms import UploadFileForm
from .models import NetflixMovie
import csv
from datetime import datetime, timedelta
from io import TextIOWrapper



# Restrict view to logged in users
@login_required(login_url='login')
def index(request):
    all_movies = Movie.objects.all()

    recently_added_movies = Movie.objects.order_by('-id')[:15]

    series = Movie.objects.filter(isSeries=True)
    movies = Movie.objects.filter(isSeries=False)

    # featured_movie = movies[len(movies)-1]
    featured_movie = Movie.objects.get(title="Black Mirror")

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
            response = {'status' : 'success', 'message': 'Added to My List'}
        else:
            response = {'status' : 'added', 'message': 'Movie already in My List'}
        
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
        
        # Try to delete the movie from user's "My List" list
        try:
            my_movie = MyMovies.objects.get(user=request.user, movie=movie)
            my_movie.delete()
            response = {'status': 'success', 'message': 'Removed from My List'}
        except MyMovies.DoesNotExist:
            response = {'status': 'not_found', 'message': 'Movie not found in My List'}
        
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

#### Netflix Wrapped Landing Page ####
# In order to get the updated user file, a restarting of the server is required
@login_required(login_url='login')
def netflix_wrapped_landing_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if file.name.endswith('.csv'):
                try:
                    UserMovie.objects.all().delete()
                    csv_file_wrapper = TextIOWrapper(file, encoding='utf-8')
                    reader = csv.DictReader(csv_file_wrapper)
                    for row in reader:
                        start_time = timezone.make_aware(datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S'))

                        # Check if the start time is within the last year
                        one_year_ago = timezone.now() - timedelta(days=365)
                        if start_time >= one_year_ago:
                            dur_hours, dur_minutes, dur_seconds = map(int, row['Duration'].split(':'))
                            duration = timedelta(hours=dur_hours, minutes=dur_minutes, seconds=dur_seconds)

                            attributes = row['Attributes']
                            title = row['Title']
                            supplemental_video_type = row['Supplemental Video Type']
                            device_type = row['Device Type']

                            book_hours, book_minutes, book_seconds = map(int, row['Bookmark'].split(':'))
                            bookmark = timedelta(hours=book_hours, minutes=book_minutes, seconds=book_seconds)

                            # Catch 'Not latest view' exception
                            latest_bookmark = timedelta(days=-1)
                            if row['Latest Bookmark'] != 'Not latest view':
                                latest_hours, latest_minutes, latest_seconds = map(int, row['Latest Bookmark'].split(':'))
                                latest_bookmark = timedelta(hours=latest_hours, minutes=latest_minutes, seconds=latest_seconds)

                            country = row['Country']

                            # Create and save NetflixMovie object
                            UserMovie.objects.create(
                                profile_name=row['Profile Name'],
                                start_time=start_time,
                                duration=duration,
                                attributes=attributes,
                                title=title,
                                supplemental_video_type=supplemental_video_type,
                                device_type=device_type,
                                bookmark=bookmark,
                                latest_bookmark=latest_bookmark,
                                country=country
                            )

                    # Get all records from the database where start time is within the last year
                    one_year_ago = timezone.now() - timedelta(days=365)
                    records_within_last_year = UserMovie.objects.filter(start_time__gte=one_year_ago)
                    print("Gathered records within the last year and sending to netflix_wrapped_landing_page.html")
                    return render(request, 'netflix_wrapped_landing_page.html', {'data': records_within_last_year})
                except Exception as e:
                    return render(request, 'netflix_wrapped_landing_page.html', {'error_message': f"Error processing CSV: {str(e)}"})
            else:
                return render(request, 'netflix_wrapped_landing_page.html', {'error_message': 'Only CSV files are allowed.'})
    else:
        form = UploadFileForm()
   
    return render(request, 'netflix_wrapped_landing_page.html', {'form': form})


# Correct Cached
# def get_cached_netflix_viewing_queryset(duration):
#     queryset_key = 'netflix_viewing_queryset'    
#     # Try to retrieve the queryset from the cache
#     netflix_viewing_queryset = cache.get(queryset_key)
#     if netflix_viewing_queryset is None:
#         X_months_ago = datetime.now() - timedelta(days=int(duration)*30)
#         netflix_viewing_queryset = NetflixMovie.objects.filter(start_time__gte=X_months_ago)
#         cache.set(queryset_key, netflix_viewing_queryset, timeout=3600)
#     return netflix_viewing_queryset

# def get_user_cached_netflix_viewing_queryset(duration):
#     queryset_key = 'user_netflix_viewing_queryset'    
#     # Try to retrieve the queryset from the cache
#     netflix_viewing_queryset = cache.get(queryset_key)
#     if netflix_viewing_queryset is None:
#         X_months_ago = datetime.now() - timedelta(days=int(duration)*30)
#         netflix_viewing_queryset = UserMovie.objects.filter(start_time__gte=X_months_ago)
#         cache.set(queryset_key, netflix_viewing_queryset, timeout=3600)
#     return netflix_viewing_queryset


def get_cached_netflix_viewing_queryset(duration):
    X_months_ago = datetime.now() - timedelta(days=int(duration)*30)
    netflix_viewing_queryset = NetflixMovie.objects.filter(start_time__gte=X_months_ago)
    return netflix_viewing_queryset

def get_user_cached_netflix_viewing_queryset(duration):
    X_months_ago = datetime.now() - timedelta(days=int(duration)*30)
    netflix_viewing_queryset = UserMovie.objects.filter(start_time__gte=X_months_ago) 
    return netflix_viewing_queryset

@login_required(login_url='login')
def netflix_wrapped(request):
    user = request.GET.get('user')
    duration = request.GET.get('duration')
    

    # Process the response data
    watchTimeByMonth = getWatchTimeByMonth(user, duration)
    watchTimeByDayOfWeek = getWatchTimeByDayOfWeek(user, duration)
    watchTimeByTimeOfDay = getWatchTimeByTimeOfDay(user, duration)
    top10MostWatchedTitles = getTop10MostWatchedTitles(user, duration)
    totalHoursWatched = round(getTotalHoursWatched(user, duration), 2)
    totalUniqueTitlesWatched = getTotalUniqueTitlesWatched(user, duration)
    
    context = {
        'watchTimeByMonth': watchTimeByMonth,
        'watchTimeByDayOfWeek': watchTimeByDayOfWeek,
        'top10MostWatchedTitles': top10MostWatchedTitles,
        'totalHoursWatched': totalHoursWatched,
        'totalUniqueTitlesWatched': totalUniqueTitlesWatched,
        'watchTimeByTimeOfDay': watchTimeByTimeOfDay,
    }
    return render(request, 'netflix_wrapped.html', context)
            
def getTotalHoursWatched(user, duration):
    if user.lower() == 'alex':
        netflix_viewing_queryset = get_cached_netflix_viewing_queryset(duration)
    else:
        netflix_viewing_queryset = get_user_cached_netflix_viewing_queryset(duration)

    total_hours = 0

    for viewing in netflix_viewing_queryset:
        duration_hours = viewing.duration.total_seconds() / 3600
        total_hours += duration_hours
    return total_hours

def getTotalUniqueTitlesWatched(user, duration):
    if user.lower() == 'alex':
        netflix_viewing_queryset = get_cached_netflix_viewing_queryset(duration)
    else:
        netflix_viewing_queryset = get_user_cached_netflix_viewing_queryset(duration)

    unique_titles = set()

    for viewing in netflix_viewing_queryset:
        unique_titles.add(viewing.title)

    return len(unique_titles)    

def getWatchTimeByTimeOfDay(user, duration):
    if user.lower() == 'alex':
        netflix_viewing_queryset = get_cached_netflix_viewing_queryset(duration)
    else:
        netflix_viewing_queryset = get_user_cached_netflix_viewing_queryset(duration)

    # Define time bins for different parts of the day
    time_bins = {
        'Morning (6 am to 12 pm)': range(6, 12),  # 6 am to 12 pm
        'Afternoon (12 pm to 6 pm)': range(12, 18),  # 12 pm to 6 pm
        'Night (6 pm to 12 am)': range(18, 24),  # 6 pm to 12 am
        'Demon Time (12 am to 6 am)': range(0, 6)  # 12 am to 6 am
    }

    # Initialize watch time for each time bin
    watch_time_by_time_of_day = {time_bin: 0 for time_bin in time_bins}

    # Aggregate watch time into different time bins
    for viewing in netflix_viewing_queryset:
        start_time = viewing.start_time.time()
        end_time = (viewing.start_time + viewing.duration).time()

        for time_bin, time_range in time_bins.items():
            start_hour = start_time.hour
            end_hour = end_time.hour

            # Ensure the hour values are within the range of 0 to 23
            start_hour %= 24
            end_hour %= 24

            if start_hour in time_range:
                if end_hour in time_range:  # Viewing session entirely within the time bin
                    watch_time_by_time_of_day[time_bin] += viewing.duration.total_seconds()
                else:  # Viewing session spans multiple time bins
                    if start_hour < end_hour:  # Viewing session starts and ends in different time bins
                        watch_time_by_time_of_day[time_bin] += (end_time.hour - start_time.hour) * 3600 + (end_time.minute - start_time.minute) * 60 + (end_time.second - start_time.second)
                    else:  # Viewing session starts in the current time bin and ends in the next time bin
                        watch_time_by_time_of_day[time_bin] += (24 - start_time.hour) * 3600 + (start_time.minute * 60) + (start_time.second)
                        next_time_bin = list(time_bins.keys())[(list(time_bins.keys()).index(time_bin) + 1) % len(time_bins)]
                        watch_time_by_time_of_day[next_time_bin] += (end_time.hour * 3600) + (end_time.minute * 60) + (end_time.second)

    # Convert watch time to hours
    watch_time_by_time_of_day_hours = {time_bin: watch_time / 3600 for time_bin, watch_time in watch_time_by_time_of_day.items()}

    # Create a bar chart
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=list(watch_time_by_time_of_day_hours.keys()),
        y=list(watch_time_by_time_of_day_hours.values()),
        marker_color='rgb(255, 0, 0)' 
    ))

    # Update layout
    fig.update_layout(
        title={
            'text':'Total Watch Time by Time of Day',
            'font':{'size':32}
        },
        xaxis=dict(title='Time of Day'),
        yaxis=dict(title='Watch Time (hours)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    chart = fig.to_html()
    return chart



def getTop10MostWatchedTitles(user, duration):
    if user.lower() == 'alex':
        netflix_viewing_queryset = get_cached_netflix_viewing_queryset(duration)
    else:
        netflix_viewing_queryset = get_user_cached_netflix_viewing_queryset(duration)

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
        title={
            'text':'Top 10 Most Watched Titles',
            'font':{'size':32}
        },
        xaxis=dict(title='Title'),
        yaxis=dict(title='Total Watch Time (minutes)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    chart = fig.to_html()   
    return chart

def getWatchTimeByDayOfWeek(user, duration):
    if user.lower() == 'alex':
        netflix_viewing_queryset = get_cached_netflix_viewing_queryset(duration)
    else:
        netflix_viewing_queryset = get_user_cached_netflix_viewing_queryset(duration)

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
        title={
            'text':'Total Watch Time by Day of Week',
            'font':{'size':32}
        },
        xaxis=dict(title='Day of Week'),
        yaxis=dict(title='Total Watch Time (minutes)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    chart = fig.to_html()
    return chart



def getWatchTimeByMonth(user, duration):
    if user.lower() == 'alex':
        netflix_viewing_queryset = get_cached_netflix_viewing_queryset(duration)
    else:
        netflix_viewing_queryset = get_user_cached_netflix_viewing_queryset(duration)

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
        title={
            'text':'Total Watch Time by Month',
            'font':{'size':32}
        },
        xaxis=dict(title='Month'),
        yaxis=dict(title='Total Watch Time (minutes)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    chart = fig.to_html()
    return chart



###TODO 

# The error is below right here. There is an issue with how netflix_movie is being created
# See in load_viewing_activity.py, there is additional processing to load the values into the model
    # The dates/times have to be split into hours, minutes, seconds to create datetime objects
    # Catch 'Not latest View' exception for the 'latest bookmark field'

# The code here seems to have deleted Alex's NetflixMovie objects, so that has to be reloaded 


# def upload_csv(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():

#             file = request.FILES['file']
#             print("filename =", file.name)
#             if file.name.endswith('.csv'):
#                 try:
#                     UserMovie.objects.all().delete()

#                     # Wrap the file object with TextIOWrapper and specify encoding
#                     csv_file_wrapper = TextIOWrapper(file, encoding='utf-8')

#                     reader = csv.DictReader(csv_file_wrapper)
#                     c = 0
#                     for row in reader:
#                         if c < 5: print(row['Profile Name'])
#                         c += 1
#                         start_time = timezone.make_aware(datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S'))

#                         # Check if the start time is within the last year
#                         one_year_ago = timezone.now() - timedelta(days=365)
#                         if start_time >= one_year_ago:
#                             dur_hours, dur_minutes, dur_seconds = map(int, row['Duration'].split(':'))
#                             duration = timedelta(hours=dur_hours, minutes=dur_minutes, seconds=dur_seconds)

#                             attributes = row['Attributes']
#                             title = row['Title']
#                             supplemental_video_type = row['Supplemental Video Type']
#                             device_type = row['Device Type']

#                             book_hours, book_minutes, book_seconds = map(int, row['Bookmark'].split(':'))
#                             bookmark = timedelta(hours=book_hours, minutes=book_minutes, seconds=book_seconds)

#                             # Catch 'Not latest view' exception
#                             latest_bookmark = timedelta(days=-1)
#                             if row['Latest Bookmark'] != 'Not latest view':
#                                 latest_hours, latest_minutes, latest_seconds = map(int, row['Latest Bookmark'].split(':'))
#                                 latest_bookmark = timedelta(hours=latest_hours, minutes=latest_minutes, seconds=latest_seconds)

#                             country = row['Country']

#                             # Create and save NetflixMovie object
#                             UserMovie.objects.create(
#                                 profile_name=row['Profile Name'],
#                                 start_time=start_time,
#                                 duration=duration,
#                                 attributes=attributes,
#                                 title=title,
#                                 supplemental_video_type=supplemental_video_type,
#                                 device_type=device_type,
#                                 bookmark=bookmark,
#                                 latest_bookmark=latest_bookmark,
#                                 country=country
#                             )

#                     # Get all records from the database where start time is within the last year
#                     one_year_ago = timezone.now() - timedelta(days=365)
#                     records_within_last_year = UserMovie.objects.filter(start_time__gte=one_year_ago)
#                     print("Gathered records within the last year and sending to upload.html")
#                     return render(request, 'upload.html', {'data': records_within_last_year})
#                 except Exception as e:
#                     return render(request, 'upload.html', {'error_message': f"Error processing CSV: {str(e)}"})
#             else:
#                 return render(request, 'upload.html', {'error_message': 'Only CSV files are allowed.'})
#     else:
#         form = UploadFileForm()
   
#     return render(request, 'upload.html', {'form': form})