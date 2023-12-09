import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Address
from .forms import AddressForm

logger = logging.getLogger(__name__)


@login_required
def index(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, "dashboard/index.html", {"addresses": addresses})


@login_required
def logout_view(request):
    logout(request)
    return redirect("index")


@login_required
def view_address(request, address_id):
    address = get_object_or_404(Address, id=address_id)
    logger.info(
        f"Viewing address ID {address_id} belonging to user {address.user.username} as user {request.user.username}"
    )
    return render(request, "dashboard/view_address.html", {"address": address})


@login_required
def create_address(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect("index")
    else:
        form = AddressForm()

    return render(request, "dashboard/create_address.html", {"form": form})
