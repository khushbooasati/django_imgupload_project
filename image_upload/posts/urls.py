from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.gadha_home, name='home'),
    path('index/',views.index_home,name='index'),
    path('script/',views.script_home,name='script'),
]