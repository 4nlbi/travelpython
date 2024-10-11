from django.shortcuts import render
from . models import services, portfolio,story
# Create your views here.

def demo(request):
    # Retrieve all services and portfolio items from the database
    obj = services.objects.all()
    ob = portfolio.objects.all()
    sto = story.objects.all()

    return render(request, 'index.html', {'result':obj,'op':ob,'sto':sto})
