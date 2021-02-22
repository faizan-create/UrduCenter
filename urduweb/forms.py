from django import forms
from .models import Post, Comment, Contact


class Add_Post(forms.ModelForm):
    class Meta():
        model = Post
        fields = '__all__'


class Add_Comment(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('name', 'email', 'message')


class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ('name', 'message', 'email')
