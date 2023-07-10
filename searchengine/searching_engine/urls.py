from django.contrib import admin
from django.urls import include, path
import views
from .views import HomePageView, SearchResultsView 

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
   
   
    path('search', views.searching_engine, name="index"),
    path('admin/', admin.site.urls),
    path('result', views.searching_engine, name="result") # include('searching_engine')
    # path("result", include('searching_engine'))
]

