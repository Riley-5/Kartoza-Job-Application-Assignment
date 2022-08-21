from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from portfolio_app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login

# Create your views here.
"""
    Defualt view 
    Displayes the usrs profile page
"""
def index(request):
    template = loader.get_template("portfolio_app/index.html")
    context = {
        "user": request.user
    }
    return HttpResponse(template.render(context, request))

"""
    Gets the updated profile values from the edit profile form 
    Updates that users profile information
    Returns to the index page
"""
def edit_profile(request):
    pk = request.user.id

    if request.method == "POST":
        # Get data from form
        username = request.POST["username"]
        home_address = request.POST["home_address"]
        phone_number = request.POST["phone_number"]

        # Update user in DB
        user = User.objects.get(id=pk)
        user.username = username
        user.home_address = home_address
        user.phone_number = phone_number
        user.save()

        # Route back to profile/index page
        return HttpResponseRedirect(reverse("index"))

    template = loader.get_template("portfolio_app/edit_profile.html")
    context = {
        "user_info": request.user
    }
    return HttpResponse(template.render(context, request))

"""
    Collects all the sign in information from the sign up form 
    Creates a new user and saves user to db
    Navigates back to the index page
"""
def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        home_address = request.POST["home_address"]
        phone_number = request.POST["phone_number"]
        location_latitude = request.POST["location_latitude"]
        location_longitude = request.POST["location_longitude"]

        user = User(username=username, password=password, home_address=home_address, phone_number=phone_number, location_latitude=location_latitude, location_longitude=location_longitude)
        user.save()

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "portfolio_app/sign_up.html" )


        

"""
    Renders the map with all the users as markers
"""
def map(request):
    return render(request, "portfolio_app/map.html")

"""
    API route
    Sends all the users to the frontend
"""
@csrf_exempt
def get_users(request):
    users = User.objects.all()
    return JsonResponse([user.serialize() for user in users], safe=False)