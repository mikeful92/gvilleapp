from django.shortcuts import render, get_list_or_404, HttpResponseRedirect

# Create your views here.

from .forms import AddressForm
from .models import Consumption

def home(request):
    form = AddressForm(None)
    context = {"form": form}
    template = "home.html"
    return render(request, template, context)

def results(request):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        address = form.cleaned_data['address']
        obj = get_list_or_404(Consumption, ServiceAddress=address)
    context = {"form": form, "obj": obj}
    template = "results.html"
    return render(request, template, context)

