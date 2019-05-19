from django.db import models


class Allergen(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='sandwiches/images/', blank=True, null=True)

    def __str__(self):
        return self.name


class IngredientGroup(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    group = models.ForeignKey(IngredientGroup, on_delete=models.CASCADE, null=True, blank=True)
    calories_per_portion = models.IntegerField(null=True, blank=False)
    portion_size_grams = models.IntegerField(null=True, blank=False)
    price = models.DecimalField(null=True, blank=False, decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name


class Sandwich(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    accessible = models.BooleanField(null=True)
    image = models.ImageField(upload_to='sandwiches/images/', blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name or 'nowa kanapka nr {}'.format(self.pk)
