from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from tickets.models import BusRoute, Ticket
from tickets.forms import BusRouteForm, TicketForm


def bus_route_list_view(request):
    bus_route_qs = BusRoute.objects.order_by("-updated")

    context = {"bus_route_list": bus_route_qs}
    template_name = "tickets/bus-route-list.html"

    return render(request, template_name, context)


def bus_route_create_view(request):
    if request.method == "POST":
        bus_route_create_form = BusRouteForm(request.POST)

        if bus_route_create_form.is_valid():
            bus_route_create_form.save()

            messages.info(request, "Bus route has been added")

    bus_route_create_form = BusRouteForm()

    context = {"bus_route_create_form": bus_route_create_form}
    template_name = "tickets/bus-route-create.html"

    return render(request, template_name, context)


def bus_route_details_view(request, id):
    bus_route = get_object_or_404(BusRoute, id=id)

    context = {"bus_route": bus_route}
    template_name = "tickets/bus-route-details.html"

    return render(request, template_name, context)


def bus_route_delete_view(request, id):
    bus_route = get_object_or_404(BusRoute, id=id)
    bus_route.delete()

    messages.info(request, "Bus route has been deleted")

    return redirect("tickets:bus-route-list")


@login_required
def ticket_list_view(request):
    ticket_qs = Ticket.objects.filter(user=request.user).order_by("-updated")

    context = {"ticket_list": ticket_qs}
    template_name = "tickets/ticket-list.html"

    return render(request, template_name, context)


@login_required
def ticket_create_view(request):
    if request.method == "POST":
        ticket_create_form = TicketForm(request.POST)

        if ticket_create_form.is_valid():
            if request.user.is_authenticated:
                ticket = ticket_create_form.save(commit=False)
                ticket.user = request.user
                ticket.save()
            else:
                ticket_create_form.save()

            messages.info(request, "Ticket has been booked")

            return redirect("tickets:ticket-details", ticket_create_form.instance.id)
        else:
            print(ticket_create_form.errors)

    ticket_create_form = TicketForm()

    context = {"ticket_create_form": ticket_create_form}
    template_name = "tickets/ticket-create.html"

    return render(request, template_name, context)


def ticket_details_view(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    context = {"ticket": ticket}
    template_name = "tickets/ticket-details.html"

    return render(request, template_name, context)


def ticket_delete_view(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    ticket.delete()

    messages.info(request, "Ticket has been deleted")

    return redirect("tickets:ticket-list")
