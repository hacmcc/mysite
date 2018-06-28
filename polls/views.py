from django.http.response import HttpResponse,Http404
from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    return HttpResponse("polls index!")

def current_datetime(request):
    now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html).....