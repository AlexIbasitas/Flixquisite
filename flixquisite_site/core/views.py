from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

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

