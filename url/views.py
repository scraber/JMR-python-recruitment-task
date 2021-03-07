from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView

from .forms import UrlForm
from .models import Url


def index(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            url = form.cleaned_data["full_url"]
            new_url = Url(full_url=url, code=code)
            new_url.save()
            # return HttpResponseRedirect
    else:
        form = UrlForm()
    return render(
        request,
        "url/url_form.html",
        {"form": form, "absolute_url": request.build_absolute_uri()},
    )


def redirect(request, code):
    print(f"code: {code}")
    obj = get_object_or_404(Url, code=code)
    print(f"obj: {obj}")
    return HttpResponseRedirect(obj.full_url)
