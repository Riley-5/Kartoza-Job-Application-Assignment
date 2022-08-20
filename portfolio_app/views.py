from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template("portfolio_app/index.html")
    context = {
        "user": request.user
    }
    return HttpResponse(template.render(context, request))