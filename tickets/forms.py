from django import forms

from tickets.models import BusRoute, Ticket, Destination


class BusRouteForm(forms.ModelForm):
    """
    `BusRoute` form
    """

    arrival = forms.CharField()
    departure = forms.CharField()

    class Meta:
        model = BusRoute
        fields = ["name", "arrival", "departure"]

    def clean(self):
        cleaned_data = super().clean()

        __arrival = cleaned_data["arrival"]
        __departure = cleaned_data["departure"]

        arrival, _ = Destination.objects.get_or_create(name=__arrival)
        departure, _ = Destination.objects.get_or_create(name=__departure)

        self.cleaned_data["arrival"] = arrival
        self.cleaned_data["departure"] = departure

        return super().clean()


class TicketForm(forms.ModelForm):
    """
    `Ticket` form
    """

    class Meta:
        model = Ticket
        fields = ["route"]
