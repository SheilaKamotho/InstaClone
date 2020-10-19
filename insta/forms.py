from django import forms
from .models import Image,Profile


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['editor','pub_date', 'likes','comments','profile']
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['editor']
        

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['editor','pub_date', 'likes','profile','image','caption']