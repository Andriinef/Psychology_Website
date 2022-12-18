from django.urls import include, path

from blog import views


urlpatterns = [
    path("", views.index, name="index"),
    path("aboutme/", views.aboutme, name="aboutme"),
    path("groupe/", views.group, name="groupe"),
    path("how/", views.how, name="how"),
    path("individual/", views.individual, name="individual"),
    path("base/", views.base, name="base"),
    path("valid/", views.RecordingQuestion.as_view(), name="valid"),
    path("clients_question/", views.ListClientsQuestions.as_view(), name="clients_question"),
    path("clients_question/<int:pk>/delete/", views.ClientsQuestionsDelete.as_view(), name="delete"),
    path("clients_question/<int:pk>", views.UpdateStatusQuestion.as_view(), name="clients_status"),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.Register.as_view(), name="register"),
    path("password_reset_valid/", views.password_reset_valid, name="password_reset_valid")
]
