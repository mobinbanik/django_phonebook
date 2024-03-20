from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="first name",
    )
    last_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="last name",
    )
    number = models.CharField(
        max_length=12,
        blank=False,
        null=False,
        verbose_name="number",
    )
    address = models.TextField(
        blank=False,
        null=False,
        verbose_name="address",
    )

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
