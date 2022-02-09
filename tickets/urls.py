from django.urls import path

from tickets.views import (
    bus_route_create_view,
    bus_route_delete_view,
    bus_route_details_view,
    bus_route_list_view,
    ticket_create_view,
    ticket_delete_view,
    ticket_details_view,
    ticket_list_view,
)

app_name = "tickets"

urlpatterns = [
    path("bus-route/", bus_route_list_view, name="bus-route-list"),
    path("bus-route/create/", bus_route_create_view, name="bus-route-create"),
    path(
        "bus-route/<uuid:id>/details/", bus_route_details_view, name="bus-route-details"
    ),
    path("bus-route/<uuid:id>/delete/", bus_route_delete_view, name="bus-route-delete"),
    path("", ticket_list_view, name="ticket-list"),
    path("book/", ticket_create_view, name="ticket-create"),
    path("<uuid:id>/details/", ticket_details_view, name="ticket-details"),
    path("<uuid:id>/delete/", ticket_delete_view, name="ticket-delete"),
]
