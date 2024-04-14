from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.utils.translation import gettext_lazy


class Address(models.Model):
    """A class representation of an address model

    Arguments:
        models -- Class Model

    Returns:
        None
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self) -> str:
        """The string representation of the class

        Returns:
            str: the adress
        """
        return f'{self.number} {self.street}'

    class Meta:
        """Meta class representation of an address
        """
        verbose_name_plural = gettext_lazy("Addresses")


class Letting(models.Model):
    """A class representation of a letting

    Arguments:
        models -- class: Model class

    Returns:
        None
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """The string representation of the class

        Returns:
            str: the letting title
        """
        return self.title
