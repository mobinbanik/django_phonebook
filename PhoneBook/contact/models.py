from django.db import models
from django.conf import settings


# Create your models here.
class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
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
        blank=True,
        null=True,
        verbose_name="address",
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="user",
    )

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
