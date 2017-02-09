from django.shortcuts import render
from .models import SpeechModel ,SpeechForm
from django.http import HttpResponseRedirect
# Create your views here.
def speechHome(request):
    template="speech_templates/speech.html"

    form = SpeechForm(request.POST or None)
    # print form 
    if request.method == 'POST':
        if form.is_valid():
            variable = form.save(commit='false')
            variable.save() 

            # return HttpResponseRedirect("/granite/"+str(variable.id))
            return HttpResponseRedirect("/BND/"+"&l="+str(variable.lines)+"&v="+str(variable.voice))
            
        else:
            print "SHIT SOMETHING WENT WRONG"
            # print form
            print "shit"
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
    print curnum
    wow=SpeechModel

    text= wow.objects.get(id=curnum).lines
    # print text, "wow"
    text= text.replace("\r\n"," ")
    text = text.replace('"', '')
    text = text.replace("'","") 
    print text
    voicetype= wow.objects.get(id=curnum).voice
    print voicetype
    context={ 
        "text":text,
        "voicetype":voicetype,
        
    }
    return render(request,template,context)
def BND(request, path):
    # print path
    template="speech_templates/bnd.html"

    
    voicelocation=path.index("&v=")
    line = path[3:voicelocation]
    voice= path[voicelocation+3:]
    print voice 
    
    print line
    context={
        "text": line,
        "voicetype":voice,
    }
    return render(request,template,context)
def capitalism(request, id=None):
    template="speech_templates/capitalism.html"
    
  
    context={ 
        
        
    }
    return render(request,template,context)