from django import forms

class postjob(forms.Form):
    name = forms.CharField()
    jobtype = forms.CharField()
    role = forms.CharField()
    jobdescription = forms.CharField()
    email = forms.EmailField()