from django.shortcuts import render, redirect
from logAnalyze.forms import hornetUrlForm

def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#     return render(request, 'logAnalyze/index.html')
	if request.method == 'POST':
		c = {
			'url':request.POST["hornetUrl"]
		}
		hornetUrl=request.POST["hornetUrl"]
		return redirect('logAnalyze:analyze', url=hornetUrl)
	else:
		f =  hornetUrlForm()
		c = {'hornetForm': f}
	return render(request, 'logAnalyze/index.html', c)
		#return render(request, 'logAnalyze/index.html', {'hornetform': f})

def analyze(request, url):
	#return redirect('logAnalyze:results', {'url': url})
	return render(request, 'logAnalyze/index.html', {'url': url})

def results(request, url):
#    response = "You're looking at the results of %s."
#    return HttpResponse(response % url)
     return render(request, 'logAnalyze/result.html', {'url': url})

