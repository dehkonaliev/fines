from django.shortcuts import render, redirect
from django.views import View
from .models import Fine
from django.db.models import F

class FineView(View):
    def get(self, request):
        fines = Fine.objects.all()
        total = Fine.objects.count()
        print(total)
        return render(request, 'index.html', {'fines':fines, 'total':total})
    
    def post(self, request):
        days = request.POST.getlist('days')
        fines = Fine.objects.all()
        for day in days:
            splitted = day.split('__')
            Fine.objects.filter(id__in=splitted[0]).update(days=int(splitted[1]))
        return render(request, 'index.html', {'fines':fines})
        
class Completed(View):
    def post(self, request):
        ids = request.POST.getlist('student')
        Fine.objects.filter(id__in=ids).update(days=F('days')-1)
        return redirect('home')