from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from GamingReports.models import Report
from django.core.mail import send_mail
from LiveOps.forms import ReportForm

def homepage(request):
    return HttpResponse('Homepage')

def hello(request): 
    ua = request.META['HTTP_USER_AGENT']   
    return render(request, 'hello.html', {'person_name': 'Hoppo', 'browser': ua})

def test(request):
    return render(request, 'test.html', {'person_name': 'John'})

def report(request):
    errors = []
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
	    cd = form.cleaned_data
            #add data to database
            r1 = Report(event = cd['event'], author = cd['author'], datetime = cd['datetime'], diagnosis = cd['diagnosis'], impact = cd['impact'], resolution  = cd['resolution'], responsibility = cd['responsibility'], actionable = cd['actionable'], action = cd['action'])
            r1.save()
            return HttpResponseRedirect('/report/added/')
    else:
        form = ReportForm()
    return render(request, 'report_form.html', {'form': form})

def added(request):
    return HttpResponse('Data added!')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            reports = Report.objects.filter(event__icontains=q)
            return render(request, 'search_results.html',
                {'reports': reports, 'query': q})
    return render(request, 'search_form.html',
        {'error': error})

def display_meta(request):
    values = request.META.items()
    values.sort()
    return render(request, 'display_meta.html', {'values': values})