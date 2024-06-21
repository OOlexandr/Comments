from django.forms import ModelForm, CharField, TextInput, HiddenInput
from .models import Comment


class CommentForm(ModelForm):

    username = CharField(min_length=3, max_length=10, required=True, widget=TextInput())
    email = CharField(min_length=3, max_length=20, required=True, widget=TextInput())
    text = CharField(min_length=3, max_length=500, required=True, widget=TextInput())
    
    class Meta:
        model = Comment
        fields = ['username', 'email', 'text', 'parent']
        widgets = {
            'parent': HiddenInput()
        }