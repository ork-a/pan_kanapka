from __future__ import unicode_literals

from clients.models import User
from clients.models import Company
from sandwiches.models import Allergen
from sandwiches.models import IngredientGroup
from sandwiches.models import Ingredient
from sandwiches.models import Sandwich
from orders.models import Order
from orders.models import OrderSandwiches
import csv

class DbManager:

    allergens_csv_name = "doc/demo_data_in_csv/allergens.csv"
    clients_csv_name = "doc/demo_data_in_csv/clients.csv"
    ingredient_groups_csv_name = "doc/demo_data_in_csv/ingredient_groups.csv"
    ingredients_csv_name = "doc/demo_data_in_csv/ingredients.csv"
    sandwiches_csv_name = "doc/demo_data_in_csv/sandwiches.csv"
    companies_csv_name = "doc/demo_data_in_csv/companies.csv"
    sandwich_images_path = "/sandwiches/images/s{}.jpg"

    def import_allergens(self):
        with open(self.allergens_csv_name, encoding="utf-8") as allergens_csv_file:
            csv_reader = csv.reader(allergens_csv_file, delimiter=',')
            for name in csv_reader:
                allergen = Allergen()
                allergen.name = name[0]
                allergen.save()

    def import_ingredient_groups(self):
        with open(self.ingredient_groups_csv_name, encoding="utf-8") as ingredient_groups_csv_file:
            csv_reader = csv.reader(ingredient_groups_csv_file, delimiter=',')
            for name in csv_reader:
                ingredient_group = IngredientGroup()
                ingredient_group.name = name[0]
                ingredient_group.save()

    def import_ingredients(self):
        with open(self.ingredients_csv_name, encoding="utf-8") as ingredients_csv_file:
            csv_reader = csv.reader(ingredients_csv_file, delimiter=',')
            for name, ingredient_group_name, calories_per_portion, portion_size_grams, price, allergen_names in csv_reader:
                ingredient = Ingredient()
                ingredient.name = name
                ingredient.group = IngredientGroup.objects.get(name=ingredient_group_name)
                ingredient.calories_per_portion = calories_per_portion
                ingredient.portion_size_grams = portion_size_grams
                ingredient.price = price
                ingredient.save()
                allergen_list = allergen_names.split("|")
                for allergen_name in allergen_list:
                    allergen_name = allergen_name.strip()
                    if allergen_name:
                        if Allergen.objects.filter(name=allergen_name).exists():
                            allergen = Allergen.objects.get(name=allergen_name)
                            ingredient.allergen.add(allergen)
                ingredient.save()

    def import_sandwiches(self):
        with open(self.sandwiches_csv_name, encoding="utf-8") as sandwiches_csv_file:
            csv_reader = csv.reader(sandwiches_csv_file, delimiter=',')
            for name, price, accessible, image_filename, ingredient_names in csv_reader:
                sandwich = Sandwich()
                sandwich.name = name
                sandwich.price = price
                sandwich.accessible = accessible
                sandwich.image = "/sandwiches/images/{}".format(image_filename)
                sandwich.save()
                ingredient_list = ingredient_names.split("|")
                for ingredient_name in ingredient_list:
                    ingredient_name = ingredient_name.strip()
                    if Ingredient.objects.filter(name=ingredient_name).exists():
                        ingredient = Ingredient.objects.get(name=ingredient_name)
                        sandwich.ingredients.add(ingredient)
                sandwich.save()

    def import_companies(self):
        with open(self.companies_csv_name, encoding="utf-8") as companies_csv_file:
            csv_reader = csv.reader(companies_csv_file, delimiter=',')
            for name, address in csv_reader:
                company = Company()
                company.name = name
                company.address = address
                company.save()

    def import_clients(self):
        with open(self.clients_csv_name, encoding="utf-8") as clients_csv_file:
            csv_reader = csv.reader(clients_csv_file, delimiter=',')
            for email, name, surname, active, company_name, staff, admin in csv_reader:
                client = User()
                client.email = email
                client.name = name
                client.surname = surname
                if admin in ['True', 'true']:
                    client.set_password('admin')
                else:
                    client.set_password('user')
                client.active = active
                company = Company.objects.get(name=company_name)
                client.group = company
                client.staff = staff
                client.admin = admin
                client.save()

    def delete_orders(self):
        Order.objects.all().delete()
        OrderSandwiches.objects.all().delete()

    def delete_clients(self):
        User.objects.all().delete()
        #User.objects.exclude(email="admin@kanapka.com").delete()

    def delete_companies(self):
        Company.objects.all().delete()

    def delete_allergens(self):
        Allergen.objects.all().delete()

    def delete_ingredients(self):
        Ingredient.objects.all().delete()

    def delete_ingredient_groups(self):
        IngredientGroup.objects.all().delete()

    def delete_sandwiches(self):
        Sandwich.objects.all().delete()

    def delete_all(self):
        self.delete_orders()
        self.delete_clients()
        self.delete_companies()
        self.delete_allergens()
        self.delete_ingredients()
        self.delete_ingredient_groups()
        self.delete_sandwiches()