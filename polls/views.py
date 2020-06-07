from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Harry, You reached the polls index")

# Create your views here.
