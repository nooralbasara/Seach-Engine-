from django.template import loader
from django.http import HttpResponse
from whoosh.qparser import QueryParser
from whoosh import index
from django.templatetags.static import static
import os
from django.conf import settings
from django.http import HttpResponse ,HttpResponseNotFound


def searching_engine(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())


def download(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, "../"+filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponseNotFound()


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
      results= searcher.search(q,limit=None)
      url = static(request)
      _result['hits_count'] = len(results)
      _result['index_doc_count'] = ix.doc_count()
      for hit in results:
          _result['result'].append(
             {
                'file_name':hit["file_name"],
                'content':hit.highlights("content"),
                'phone':hit["phone"],
                'email':hit["email"]
              }
             )
          
  template = loader.get_template('result.html')
  return HttpResponse(template.render({'search_tearm':query,'search_result':_result}))

