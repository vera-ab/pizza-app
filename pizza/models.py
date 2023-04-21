from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=False)
    ingredients = models.ManyToManyField(Ingredient, related_name='pizza_Ingredient')
    price = models.FloatField(verbose_name=_("Price"), blank=True, null=False, default=50.0)
    is_custom = models.BooleanField(verbose_name=_("Is it custom"), blank=False, null=False)

    def __str__(self):
        return self.title    


class Order(models.Model):
    date_time = models.DateTimeField(verbose_name=_("Order date and time"), auto_now_add=True)
    pizza = models.ForeignKey("Pizza", verbose_name=_("Order pizza"), blank=False, null=False, related_name="sale_product", on_delete=models.PROTECT)
    price = models.FloatField(verbose_name=_("Price"), blank=True, null=False, default=50.0)
    phone_number = models.CharField(null=False, blank=False, unique=True,help_text='Contact phone number', max_length=20)
    name = models.CharField(null=False, blank=True, unique=False,help_text='Contact name', max_length=255)
    comments = models.TextField(blank=True, null=False)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Order")

    def __str__(self):
        return f"{self.pizza}"