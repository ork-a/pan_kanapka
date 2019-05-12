
import csv

from PanKanapka.clients.models import ClientManager

class DbFromCsvImporter:
    ClientsCsvFileName = "Clients.csv"

    def ImportClients(self):
        with open(self.ClientsCsvFileName) as ClientsCsvFile:
            csv_reader = csv.reader(ClientsCsvFile, delimiter=',')
            for row in csv_reader:
                print (row[0], row[1], row[2])
                client_manager = ClientManager()
                client_manager.create_user(row[0])


