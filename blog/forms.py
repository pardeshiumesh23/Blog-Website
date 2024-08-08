from django import forms
from .models import PostModel,Comment 

class PostModelForm(forms.ModelForm):
    content= forms.CharField(widget=forms.Textarea(attrs={'rows':10}))
    class Meta:
        model = PostModel
        fields =['title','summary','image_url','content'] #use this form in views.py

class PostUpdateForms(forms.ModelForm):
    class Meta:
        model = PostModel
        fields =['title','summary','image_url','content']

class CommentForm(forms.ModelForm):
    content= forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Add Comment here...'}))
    class Meta:
        model = Comment
        fields = ("content",)