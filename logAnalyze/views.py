from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from logAnalyze.forms import hornetUrlForm

def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#     return render(request, 'logAnalyze/index.html')
	if request.method == 'POST':
		c = {
			'url':request.POST["hornetUrl"]
		}
	else:
		f =  hornetUrlForm()
		c = {'hornetForm': f}
	return render_to_response('logAnalyze/index.html', c)
		#return redirect('logAnalyze:result', {'hornetform': f})
		#return render(request, 'logAnalyze/index.html', {'hornetform': f})

def results(request, url):
#    response = "You're looking at the results of %s."
#    return HttpResponse(response % url)
     return render(request, 'logAnalyze/result.html', {'url': url})

