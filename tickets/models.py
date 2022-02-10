from django.db import models
from django.contrib.auth import get_user_model

from bus_ts.utils import BaseModel, generate_code


# user model

User = get_user_model()


class Destination(BaseModel):
    """
    Reuseable location Model for arrival/departure and other location related fields
    """

    name = models.CharField(max_length=300, unique=True)

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"

    def __str__(self):
        return self.name


class BusRoute(BaseModel):

    name = models.CharField(max_length=255, unique=True)
    arrival = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="arrival"
    )
    departure = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="departure"
    )
    price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Bus route"
        verbose_name_plural = "Bus routes"

    def __str__(self):
        return self.name

    def add_arrival_and_departure(self, arrival, departure):
        """
        Add Bus Router arrival and departure
        """
        __arrival, _ = Destination.objects.get_or_create(name=arrival)
        __departure, _ = Destination.objects.get_or_create(name=departure)

        # set arrival and departure

        self.arrival = __arrival
        self.departure = __departure

        self.save()


class Ticket(BaseModel):
    class STATUS(models.TextChoices):
        """
        Status indication `CONSTANTS` to check ticket status
        """

        READY = "READY", "Ready"
        CHECK_IN = "CHECK_IN", "Check In"
        CHECK_OUT = "CHECK_OUT", "Check Out"

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, blank=True, unique=True)
    status = models.CharField(max_length=10, default=STATUS.READY)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return self.route.name

    def save(self, *args, **kwargs):
        # generate code if code is empty
        if not self.code:
            self.code = generate_code(5).upper()

        super().save(*args, **kwargs)
