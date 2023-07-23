from django.contrib import admin
from django.urls import path
from .views import searching_engine,search_result, download
#from searching_engine import views

urlpatterns = [
    path("", searching_engine, name="search"),
    path("result", search_result, name="search_result"),
    path("download/<path:filename>",download)
    #path('download/', views.download_file),
]

