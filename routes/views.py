from django.shortcuts import render

def Home(request):
    user = request.user
    return render(request, "routes/home.html")
# Create your views here.
