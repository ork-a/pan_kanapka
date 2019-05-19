from clients.models import User
from clients.models import Company
from sandwiches.models import Allergen
from sandwiches.models import Ingredient
from sandwiches.models import Sandwich
import csv


class DbManager:

    allergens_csv_name = "doc/demo_data_in_csv/allergens.csv"
    clients_csv_name = "doc/demo_data_in_csv/clients.csv"
    ingredients_csv_name = "doc/demo_data_in_csv/ingredients.csv"
    sandwiches_csv_name = "doc/demo_data_in_csv/sandwiches.csv"
    companies_csv_name = "doc/demo_data_in_csv/companies.csv"

    def import_clients(self):
        with open(self.clients_csv_name) as clients_csv_file:
            csv_reader = csv.reader(clients_csv_file, delimiter=',')
            for email, name, surname, active, group, staff, admin in csv_reader:
                client = User()
                client.email = email
                client.name = name
                client.surname = surname
                client.active = active
#               client.grupa = group
                client.staff = staff
                client.admin = admin
                client.save()

    def import_allergens(self):
        with open(self.allergens_csv_name) as allergens_csv_file:
            csv_reader = csv.reader(allergens_csv_file, delimiter=',')
            for row in csv_reader:
                allergen = Allergen()
                allergen.name = row[0]
                allergen.save()

    def import_ingredients(self):
        with open(self.ingredients_csv_name) as ingredients_csv_file:
            csv_reader = csv.reader(ingredients_csv_file, delimiter=',')
            for row in csv_reader:
                ingredient = Ingredient()
                ingredient.name = row[0]
                ingredient.group = None
                ingredient.calories_per_portion = row[1]
                ingredient.portion_size_grams = row[2]
                ingredient.price = row[3]
                ingredient.save()

    def import_sandwiches(self):
        with open(self.sandwiches_csv_name) as sandwiches_csv_file:
            csv_reader = csv.reader(sandwiches_csv_file, delimiter=',')
            for row in csv_reader:
                sandwich = Sandwich()
                sandwich.name = row[0]
                sandwich.price = row[1]
                sandwich.accessible = row[2]
#                sandwich.ingredients.set(None)
                sandwich.save()

    def import_companies(self):
        with open(self.companies_csv_name) as companies_csv_file:
            csv_reader = csv.reader(companies_csv_file, delimiter=',')
            for name, address in csv_reader:
                company = Company()
                company.name = name
                company.address = address
                company.save()

    def delete_clients(self):
        client = User()
        client.objects.all().delete()






