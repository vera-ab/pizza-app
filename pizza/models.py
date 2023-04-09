from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Pizza(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey("Category", verbose_name=_("Product category"), blank=False, null=False, related_name="product_category", on_delete=models.PROTECT)
    ingredients = models.ManyToManyField(Ingredient, related_name='pizza_Ingredient')
    price = models.FloatField(verbose_name=_("Price"), blank=False, null=False)

    def __str__(self):
        return self.title    


class Category(models.Model):
    title = models.CharField(verbose_name=_("Category title"), max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f"{self.title}"
    

class Order(models.Model):
    date_time = models.DateTimeField(verbose_name=_("Order date and time"), auto_now_add=True)
    pizza = models.ForeignKey("Pizza", verbose_name=_("Order pizza"), blank=False, null=False, related_name="sale_product", on_delete=models.PROTECT)
    price = models.FloatField(verbose_name=_("Price"), blank=False, null=False)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Order")

    def __str__(self):
        return f"{self.pizza}"