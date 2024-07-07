from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

texts = ["God of War was first released in North America on March 22, 2005, for the PlayStation 2.",
        "God of War II was first released in North America on March 13, 2007, for the PlayStation 2.",
        "God of War III was first released in North America on March 16, 2010, for the PlayStation 3."]

def section(request, num):
    if 1 <= num <= 3: # check if the section number is valid
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")

