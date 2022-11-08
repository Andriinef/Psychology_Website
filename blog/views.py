from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")

def aboutme(request):
    return render(request, "aboutme.html")

def group(request):
    return render(request, "group.html")

def how(request):
    return render(request, "how.html")

def individual(request):
    return render(request, "individual.html")
