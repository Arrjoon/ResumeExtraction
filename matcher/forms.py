from django import forms

class JobDescriptionForm(forms.Form):
    job_description = forms.CharField(widget=forms.Textarea)
    resumes = forms.FileField()
