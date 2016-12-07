from django.shortcuts import render
from .models import SpeechModel ,SpeechForm
# Create your views here.
def speechHome(request):
    template="speech_templates/speech.html"

    form = SpeechForm(request.POST or None)
    if form.is_valid():
        variable = form.save(commit='false')
        variable.save() 
    else:
        print "SHIT SOMETHING WENT WRONG"
    wow=SpeechModel
    # print wow.objects.all()[0]


    context={ 
        "formvar": form,
        "wow":wow,
        
    }
    return render(request,template,context)