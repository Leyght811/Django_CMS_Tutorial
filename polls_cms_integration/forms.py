from django import forms

from polls.models import Question


class PollWizardForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = []