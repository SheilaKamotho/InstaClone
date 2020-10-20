from django import forms
from .models import Image,Profile, Comment


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['editor','pub_date', 'likes','comment','profile','name']
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['editor']
        

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['editor']