from django import forms

class loginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class contactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
    # attachment=forms.FileField(blank=True)
