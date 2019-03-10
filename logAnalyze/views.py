from django.shortcuts import render
from django.http import HttpResponse
from logAnalyze.forms import hornetUrlForm

def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#     return render(request, 'logAnalyze/index.html')
	f =  hornetUrlForm()
	return render(request, 'logAnalyze/index.html', {'form1': f})

def results(request, url):
#    response = "You're looking at the results of %s."
#    return HttpResponse(response % url)
     return render(request, 'logAnalyze/result.html', {'url': url})

