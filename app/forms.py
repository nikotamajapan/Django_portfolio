from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='name')
    email = forms.EmailField(max_length=100, label='email')
    message = forms.CharField(label = 'message', widget=forms.Textarea())

