from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import NameForm, ContactForm


@permission_required("contacts.add_contact")
def create(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['subject']
            form.save()
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))
    else:
        form = ContactForm()
    return render(request, 'contacts/create.html', {'form': form})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['your_name']
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "contacts/name.html", {"form": form})


def thanks(name):
    return HttpResponse(f"Obrigado {name}")
