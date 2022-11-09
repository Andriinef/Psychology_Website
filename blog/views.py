from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from blog.forms import UserCreationForm


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

def question(request):
    return render(request, "question.html")

def base(request):
    return render(request, "registration/base.html")


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, username= username, password=password)
            login(request, user)
            return redirect('base')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
