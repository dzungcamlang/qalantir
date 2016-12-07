from django.shortcuts import render
from .models import SpeechModel ,SpeechForm
from django.http import HttpResponseRedirect
# Create your views here.
def speechHome(request):
    template="speech_templates/speech.html"

    form = SpeechForm(request.POST or None)
    if form.is_valid():
        variable = form.save(commit='false')
        variable.save() 
        print variable.id,"formid"
        redirectstring="/granite/"+str(variable.id)
        print redirectstring
        return HttpResponseRedirect("/granite/"+str(variable.id))
        
    else:
        print "SHIT SOMETHING WENT WRONG"
    wow=SpeechModel
    # print wow.objects.all()[0]
    context={ 
        "formvar": form,
        "wow":wow,
        
    }
    return render(request,template,context)

def speechGranite(request, id=None):
    template="speech_templates/granite.html"


    curnum= int(id)
    wow=SpeechModel

    text= wow.objects.get(id=curnum).lines
    # print text, "wow"
    text= text.replace("\r\n"," ")
    print text
    voicetype= wow.objects.get(id=curnum).voice
    context={ 
        "text":text,
        "voicetype":voicetype,
        
    }
    return render(request,template,context)