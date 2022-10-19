from django import forms
from .models import ChatModel

class ChatForm(forms.ModelForm):
    class Meta:
        model=ChatModel
        fields='__all__'

        widgets={
            'user':forms.TextInput(attrs={'type':'hidden'})
        }