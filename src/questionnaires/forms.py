from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    """Answer model form."""
    answer=forms.CharField(required=True,widget=forms.Textarea())
    class Meta():
        model=Answer
        fields={"answer"}
