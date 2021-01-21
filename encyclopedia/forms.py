from django import forms

class NewEntry(forms.Form):
    title = forms.CharField(label='Page title:', max_length=255)
    content = forms.CharField(label='Content:', widget=forms.Textarea)

class EditEntry(forms.Form):
    content = forms.CharField(label='Content:', widget=forms.Textarea)
