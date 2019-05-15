#from PanKanapka.clients.test_importu import Test
from clients.models import Uzytkownik
from bulka.models import Alergeny
from bulka.models import Skladniki
from bulka.models import Kanapki

import csv


class DbManager:

    allergens_csv_name = "doc/demo_data_in_csv/allergens.csv"
    clients_csv_name = "doc/demo_data_in_csv/clients.csv"
    ingredients_csv_name = "doc/demo_data_in_csv/ingredients.csv"
    sandwiches_csv_name = "doc/demo_data_in_csv/sandwiches.csv"

    def import_clients(self):
        with open(self.clients_csv_name) as clients_csv_file:
            csv_reader = csv.reader(clients_csv_file, delimiter=',')
            for email, name, surname, active, group, staff, admin in csv_reader:
                client = Uzytkownik()
                client.email = email
                client.imie = name
                client.nazwisko = surname
                client.aktywny = active
#               client.grupa = group
                client.obsluga = staff
                client.admin = admin
                client.save()

    def import_allergens(self):
        with open(self.allergens_csv_name) as allergens_csv_file:
            csv_reader = csv.reader(allergens_csv_file, delimiter=',')
            for name in csv_reader:
                allergen = Alergeny()
                allergen.Ale_Nazwa = name
                allergen.save()

    def import_ingredients(self):
        with open(self.ingredients_csv_name) as ingredients_csv_file:
            csv_reader = csv.reader(ingredients_csv_file, delimiter=',')
            for group, name, archive, kcal, weight_per_portion, dummy, price in csv_reader:
                ingredient = Skladniki()
                ingredient.Skl_Grupa = group
                ingredient.Skl_Nazwa = name
                ingredient.Skl_Kcal = kcal
                ingredient.Skl_GramNaPorcje = weight_per_portion
                ingredient.Skl_Cena = price
   #             ingredient.save()

    def import_sandwiches(self):
        with open(self.sandwiches_csv_name) as sandwiches_csv_file:
            csv_reader = csv.reader(sandwiches_csv_file, delimiter=',')
            for price, archive, name, d1, d2, d3, d4, d5, d6, d7 in csv_reader:
                sandwich = Kanapki()
                sandwich.Kan_Cena = price
                sandwich.Kan_Archiwalny = archive
                sandwich.save()


    def delete_clients(self):
        client = Uzytkownik()
        client.objects.all().delete()






