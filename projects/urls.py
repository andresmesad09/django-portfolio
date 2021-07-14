from django.urls import path
from projects import views

urlpatterns = [
    # /projects
    path('', views.project_list)

]