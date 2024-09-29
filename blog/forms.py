from django import forms
from .models import FeeedbackMessage
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeeedbackMessage
        fields = ["name","email","message"]