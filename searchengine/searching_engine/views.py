from django.template import loader
from django.http import HttpResponse
import Searcher
from django.views.generic import TemplateView, ListView
from .models import Search_engine

def searching_engine(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())

def result(request):
  template = loader.get_template('result.html')
  return HttpResponse(template.render(Searcher))


class HomePageView(TemplateView):
    template_name = 'homepage.html'

class SearchResultsView(ListView):
    model = Search_engine  
    template_name = 'result.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Search_engine.objects.filter(
            query(name__icontains=query) | query(state__icontains=query)
        )
        return object_list
    







