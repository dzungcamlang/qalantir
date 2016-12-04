from django import forms 
from django.forms import ModelForm

from .models import ChromeModel

class ChromePosts(forms.ModelForm):
    class Meta:
        model = ChromeModel
        #fields= ['title','context','after','initial']
        fields=['user','msg']
    def __init__(self, *args, **kwargs):
        super(ChromePosts, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['placeholder'] ='Please insert the company name here'
        self.fields['user'].label='' #this erases the item tag
        self.fields['msg'].widget.attrs['placeholder'] ='Your name here'
        self.fields['msg'].label='' #this erases the item tag


