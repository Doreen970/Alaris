from django import forms
from .models import TalkMessage

class TalkMessageForm(forms.ModelForm):
    class Meta:
        model = TalkMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 rounded-xl border'
            })
        }