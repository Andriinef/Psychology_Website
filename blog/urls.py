from django.urls import include, path, re_path

from blog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aboutme/", views.aboutme, name="aboutme"),
    path("groupe/", views.group, name="groupe"),
    path("how/", views.how, name="how"),
    path("individual/", views.individual, name="individual"),
    path("base/", views.base, name="base"),
    path("valid/", views.valid, name="valid"),
    path("question/", views.ListRepair.as_view(), name="question"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.Register.as_view(), name="register"),
    path("add_question/", views.AddQuestion.as_view(), name="add_question"),
]
