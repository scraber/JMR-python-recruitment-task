from django import forms
from django.core.validators import RegexValidator


class UrlForm(forms.Form):
    code = forms.CharField(
        required=False,
        label="Custom Code (Optional)",
        help_text="Will be generated automatically if empty or already exists",
        max_length=100,
        validators=[
            RegexValidator(
                regex=r"^[-a-zA-Z0-9_]+$",
                message="Code can only contain hyphens, lowercase/uppercase letters, numbers and underscores",
            )
        ],
    )

    full_url = forms.URLField(
        required=True,
        label="Full URL to shorten to",
        widget=forms.URLInput(
            attrs={
                "placeholder": "https://docs.djangoproject.com/en/3.1/",
                "required": "true",
            },
        ),
    )