from rest_framework.serializers import ModelSerializer

from chrome.models import *

class ChromeSerializer(ModelSerializer):
    class Meta:
        model = ChromeModel
        fields=[
            'user',
            'msg',
            ]
