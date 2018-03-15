from django.shortcuts import render

from .models import Accident

def accidents(request):
    accidents = Accident.objects.all()
    
    context = {
        'accidents': accidents
    }

    template_name = "accidents.html"
    return render(request, template_name, context)
