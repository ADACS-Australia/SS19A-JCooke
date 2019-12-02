from django import forms

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class VerifyForm(forms.Form):
    code = forms.CharField(widget=forms.HiddenInput())
    captcha = ReCaptchaField(widget=ReCaptchaV3)
