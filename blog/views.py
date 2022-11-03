from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def aboutme(request):
    return render(request, "blog/aboutme.html")
