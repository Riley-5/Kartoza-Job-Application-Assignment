from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from portfolio_app.models import *
from django.views.decorators.csrf import csrf_exempt

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