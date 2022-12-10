from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from blog.forms import UpdateStatusQuestionFofm, UserCreationForm, RecordingQuestionFofm
from blog.models import Clients, Status
from django.db.models import Q


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


def base(request):
    return render(request, "registration/base.html")


def password_reset_valid(request):
    return render(request, "registration/base.html")


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


class RecordingQuestion(CreateView):
    """Recording new questions in the database"""
    form_class = RecordingQuestionFofm
    template_name = "valid.html"
    success_url = reverse_lazy("valid")


class ListClientsQuestions(ListView):
    """Display a list of customer questions"""
    model = Clients
    template_name = "blog/clients_question.html"
    context_object_name = "all_question"
    paginate_by = 100

    def get_queryset(self, *args, **kwargs):
        filter = Clients.objects.order_by("-date_created")
        return filter


class UpdateStatusQuestion(UpdateView):
    """Updata the status of a question"""
    model = Clients
    form_class = UpdateStatusQuestionFofm
    success_url = reverse_lazy("clients_question")


class ClientsQuestionsDelete(DeleteView):
    model = Clients
    template_name = "blog/delete.html"
    context_object_name = "client"
    success_url = reverse_lazy("clients_question")


class SearchResultsView(ListView):
    model = Clients
    template_name = "blog/search.html"
    context_object_name = "all_question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = f"search={self.request.GET.get('search')}&"
        return context

    def get_queryset(self):
        query = self.request.GET.get('search', None)
        object_list = Clients.objects.filter(Q(username__icontains=query) | Q(phone__icontains=query) | Q(question__icontains=query))
        return object_list
