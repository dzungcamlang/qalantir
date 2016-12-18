from __future__ import unicode_literals
from django.db import models
from django import forms 
from django.forms import ModelForm

temp=["UK English Female", "UK English Male", "US English Female", "Arabic Male", "Arabic Female", "Armenian Male", "Australian Female", "Brazilian Portuguese Female", "Chinese Female", "Chinese (Hong Kong) Female", "Chinese Taiwan Female", "Czech Female", "Danish Female", "Deutsch Female", "Dutch Female", "Finnish Female", "French Female", "Greek Female", "Hatian Creole Female", "Hindi Female", "Hungarian Female", "Indonesian Female", "Italian Female", "Japanese Female", "Korean Female", "Latin Female", "Norwegian Female", "Polish Female", "Portuguese Female", "Romanian Male", "Russian Female", "Slovak Female", "Spanish Female", "Spanish Latin American Female", "Swedish Female", "Tamil Male", "Thai Female", "Turkish Female", "Afrikaans Male", "Albanian Male", "Bosnian Male", "Catalan Male", "Croatian Male", "Czech Male", "Danish Male", "Esperanto Male", "Finnish Male", "Greek Male", "Hungarian Male", "Icelandic Male", "Latin Male", "Latvian Male", "Macedonian Male", "Moldavian Male", "Montenegrin Male", "Norwegian Male", "Serbian Male", "Serbo-Croatian Male", "Slovak Male", "Swahili Male", "Swedish Male", "Vietnamese Male", "Welsh Male", "US English Male", "Fallback UK Female"]
new=[]
for x in xrange(len(temp)):
    new.append([temp[x],temp[x]])


class SpeechModel(models.Model): ### lets
    id = models.AutoField(primary_key=True) 
    lines =models.TextField(max_length=1000)
    voice=models.CharField(max_length=50,choices=new,default="French Female")
    def __unicode__(self):   
        return self.lines
##### Form Handler
class SpeechForm(forms.ModelForm):
    class Meta:
        model =SpeechModel
        #fields= ['title','context','after','initial']
        fields=['lines','voice']
    def __init__(self, *args, **kwargs):
        super(SpeechForm, self).__init__(*args, **kwargs)
        self.fields['lines'].widget.attrs['placeholder'] ='Type your speech here. Press Preview to preview. Press Submit to create a unique url.'
        self.fields['lines'].label='' #this erases the item tag
    
        self.fields['voice'].label='' #this erases the item tag



