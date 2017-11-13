from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Title','class':'form-control','style':'width:400px;'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Whats on your Mind!', 'style':'resize:none;width:400px;height:200px','class':'form-control'}))
    pic = forms.FileField(required=False)

    class Meta:
        model = Blog
        fields = ['title','content','pic']


class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
