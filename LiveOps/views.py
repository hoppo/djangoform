from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from GamingReports.models import Report
from LiveOps.forms import ReportForm

def homepage(request):
    return HttpResponse('Homepage')

def display_report(request, id):
    try:
        id = int(id)
    except ValueError:
        raise Http404()
    report = Report.objects.get(id=id)
    return render(request, 'report.html', {'report_id': id, 'report': report})

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
