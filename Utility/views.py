from django.shortcuts import render, get_list_or_404, HttpResponseRedirect

# Create your views here.

from .forms import AddressForm
from .models import Electric, Water


def cleanData(address):
    address = address.upper()
    notAllowed = ['GAINESVILLE', 'FL', 'FLORIDA', ',']
    for word in notAllowed:
        if word in address:
            address = address.replace(word, '')
    addrDict = {"NORTHWEST": "NW",
                "NORTHEAST": "NE",
                "SOUTHWEST": "SW",
                "SOUTHEAST": "SE",
                "TERRACE": "TER",
                "STREET": "ST",
                "AVENUE": "AVE",
                "PLACE": "PL",
                "BOULEVARD": "BLVD",
                "DRIVE": "DR",
                "CIRCLE": "CIR",
                "COURT": "CT",
    }
    for key, value in addrDict.iteritems():
        if key in address:
            address = address.replace(key, value)
    return address

def home(request):
    form = AddressForm(None)
    context = {"form": form}
    template = "home.html"
    return render(request, template, context)

def results(request):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        address = form.cleaned_data['address']
        address = cleanData(address)
        try:
            electricObj = get_list_or_404(Electric, ServiceAddress=address)
            waterObj = get_list_or_404(Water, ServiceAddress=address)
            context = {"form": form, "electricObj": electricObj, "waterObj": waterObj}
        except:
            context = {"form": form, "address": address}
    template = "results.html"
    return render(request, template, context)

