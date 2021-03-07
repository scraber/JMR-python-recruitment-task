from django import forms


class UrlForm(forms.Form):
    code = forms.CharField(
        required=False,
        label="Custom Code (Optional)",
        help_text="Will be generated automatically if empty or already exists",
        max_length=100,
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