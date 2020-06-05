from django import forms

from . import models
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class contactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(api_params={'hl':'en'}))
    class Meta:
        model = models.Contact
        fields = ('name', 'email', 'message')
