from django.urls import path

from . import views

app_name = 'pull'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('run', views.run, name = 'run')
	]