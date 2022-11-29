from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from django import forms

from blog.forms import Add_Question_Fofm, UserCreationForm, Clients_List_Fofm
from blog.models import Clients, Status
import re


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


def valid(request):
    return render(request, "valid.html")


def base(request):
    return render(request, "registration/base.html")


def edit(request, id):
    try:
        client = Clients.objects.get(id=id)

        if request.method == "POST":
            client.status = redirect.POST.get("status")
            client.save()
            return render(request, "blog/clients_list.html")
        else:
            return render(request, "blog/client_list.html")
    except Clients.DoesNotExist:
        return render(request, "blog/client_list.html")


class Register(View):
    template_name = "registration/register.html"

    def get(self, request):
        context = {"form": UserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect("base")
        context = {"form": form}
        return render(request, self.template_name, context)


class ListRepair(ListView):
    model = Clients
    template_name = "blog/clients_list.html"
    context_object_name = "all_question"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        filter = Clients.objects.order_by("-date_created")
        return filter


class AddQuestion(CreateView):
    form_class = Add_Question_Fofm
    template_name = "blog/error_contact.html"
    success_url = reverse_lazy("valid")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Clients_List(CreateView):
   pass
