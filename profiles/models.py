from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """A class to represent a profile model

    Arguments:
        models -- object: Model

    Returns:
        None
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self) -> str:
        """Method to represent the string representation of
        a profile model

        Returns:
            str: the username
        """
        return self.user.username
