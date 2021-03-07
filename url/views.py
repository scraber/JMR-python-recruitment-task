from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import CreateView

from .forms import UrlForm
from .models import Url


def index(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"].lower()
            url = form.cleaned_data["full_url"]
            new_url = Url(full_url=url)
            new_url.save()
            # return HttpResponseRedirect
    else:
        form = UrlForm()
    return render(
        request,
        "url/url_form.html",
        {"form": form, "absolute_url": request.build_absolute_uri()},
    )
