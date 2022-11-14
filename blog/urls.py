from django.urls import path, re_path
from django.urls import include
from blog import views


urlpatterns = [
    path('', views.index, name="index"),
    path('aboutme/', views.aboutme, name="aboutme"),
    path('groupe/', views.group, name="groupe"),
    path('how/', views.how, name="how"),
    path('individual/', views.individual, name="individual"),
    path('base/', views.base, name="base"),
    path('question/', views.question, name="question"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),
]
