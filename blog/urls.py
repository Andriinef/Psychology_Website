from django.urls import path, re_path
from blog import views


urlpatterns = [
    path('', views.index, name="home"),
    path('aboutme.html/', views.aboutme, name="aboutme"),
    path('group.html/', views.group, name="group"),
    path('how.html/', views.how, name="how"),
    path('individual.html/', views.individual, name="individual"),
]
