from django.db import models


class Allergen(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='allergens/images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Alergen'
        verbose_name_plural = 'Alergeny'

    def __str__(self):
        return self.name


class IngredientGroup(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Grupa składników'
        verbose_name_plural = 'Grupy składników'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    group = models.ForeignKey(IngredientGroup, on_delete=models.CASCADE)
    calories_per_portion = models.IntegerField(null=True, blank=False)
    portion_size_grams = models.IntegerField(null=True, blank=False)
    price = models.DecimalField(null=True, blank=False, decimal_places=2, max_digits=5)
    allergen = models.ManyToManyField(Allergen)

    class Meta:
        verbose_name = 'Składnik'
        verbose_name_plural = 'Składniki'

    def __str__(self):
        return self.name


class Sandwich(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    accessible = models.BooleanField(null=True)
    image = models.ImageField(upload_to='sandwiches/images/', blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient)

    class Meta:
        verbose_name = 'Kanapka'
        verbose_name_plural = 'Kanapki'

    def get_allergens(self):
        allergens = []
        allergens_all = [list(ingredient.allergen.all()) for ingredient in self.ingredients.all()]
        for allergen_set in allergens_all:
            allergens.extend(allergen_set)
        return set(allergens)

    def __str__(self):
        return self.name or 'nowa kanapka nr {}'.format(self.pk)
