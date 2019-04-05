from django.shortcuts import render, redirect
from logAnalyze.forms import hornetUrlForm
from logAnalyze.models import Log

def index(request):
	if request.method == 'POST':
		hornetUrl=request.POST["hornetUrl"]
		return redirect('logAnalyze:analyze', url=hornetUrl)
	else:
		f =  hornetUrlForm()
		c = {'hornetForm': f}
	logs = Log.objects.all().order_by('-id')
	c['logs'] = logs
	return render(request, 'logAnalyze/index.html', c)


def analyze(request, url):
	print("URL=%s" % url)
	log = Log(url=url, status=1)
	log.save()
	return redirect('logAnalyze:index')
#	return render(request, 'logAnalyze/index.html', {'url': url})


def results(request, url):
     return render(request, 'logAnalyze/result.html', {'url': url})

