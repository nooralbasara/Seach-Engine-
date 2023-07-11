from django.contrib import admin
from django.urls import include, path
# from .views import HomePageView, SearchResultsView 
from .views import searching_engine,search_result

urlpatterns = [
    path("", searching_engine, name="search"),
    path("result", search_result, name="search_result"),
    # path("", HomePageView.as_view(), name="home"),
   
   
    # path('search', views.searching_engine, name="index"),
    # path('result', views.searching_engine, name="result") # include('searching_engine')
    # path("result", include('searching_engine'))
]

