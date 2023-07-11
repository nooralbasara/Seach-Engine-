from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Search_engine

from whoosh.qparser import QueryParser
from whoosh import index


def searching_engine(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())

def search_result(request):
  query = request.GET.get('q','')
  _result = {
     'hits_count':0,
      'result':[]
      }

  ix = index.open_dir("../index")
  with ix.searcher() as searcher:
      qp = QueryParser("content", ix.schema)
      q = qp.parse(query)
      results = searcher.search(q)
      _result['hits_count'] = len(results)
      for hit in results:
          _result['result'].append(
             {'file_name':hit["file_name"],
              'content':hit.highlights("content")}
             )

  template = loader.get_template('result.html')
  return HttpResponse(template.render({'search_tearm':query,'search_result':_result}))








# class HomePageView(TemplateView):
#     template_name = 'homepage.html'

# class SearchResultsView(ListView):
#     model = Search_engine  
#     template_name = 'result.html'

#     def get_queryset(self): # new
#         query = self.request.GET.get("q")
#         object_list = Search_engine.objects.filter(
#             query(name__icontains=query) | query(state__icontains=query)
#         )
#         return object_list
    

