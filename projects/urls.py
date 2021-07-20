from django.urls import path
from projects import views

urlpatterns = [
    # /projects
    path('', views.all_projects),

]