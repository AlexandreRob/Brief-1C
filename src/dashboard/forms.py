from django import forms
from .models import *

class UploadFileForm(forms.Form):
    file = forms.FileField()