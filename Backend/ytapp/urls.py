from django.urls import path,include
from . import views


urlpatterns = [
    path("download/", views.donloadVideo , name="download_Video")
]
