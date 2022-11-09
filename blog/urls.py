from django.urls import path, re_path
from django.urls import include
from blog import views


urlpatterns = [
    path('', views.index, name="home"),
    path('aboutme/', views.aboutme, name="aboutme"),
    path('group/', views.group, name="group"),
    path('how/', views.how, name="how"),
    path('individual/', views.individual, name="individual"),
    path('base/', views.base, name="base"),
    path('question/', views.question, name="question"),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('register/', views.Register.as_view(), name='register'),
]
