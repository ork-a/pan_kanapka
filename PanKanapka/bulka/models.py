from django.db import models

from django.db import models

class Alergeny(models.Model):
    Ale_Id = models.IntegerField(primary_key = True)
    Ale_Nazwa = models.TextField(null = True)
    Ale_Ikona = models.BinaryField(null = True)

class Skladniki(models.Model):
    Skl_Id = models.IntegerField(primary_key = True)
    Skl_Grupa = models.IntegerField()
    Skl_Nazwa = models.TextField(null = True)
    Skl_Archiwalny = models.IntegerField(null = True)
    Skl_Kcal = models.IntegerField(null = True)
    Skl_GramNaPorcje = models.IntegerField(null = True)
    Skl_Cena = models.IntegerField(null = True)
    Skl_Ikona = models.BinaryField(null = True)
	
class Kanapki(models.Model):
    Kan_Id = models.IntegerField(primary_key = True)
    Kan_Cena = models.FloatField(null = True)
    Kan_Archiwalny = models.IntegerField(null = True)
    KaS_Ikona = models.BinaryField(null = True)

class SkladnikiAlergeny(models.Model):
    SklA_Id = models.IntegerField(primary_key = True)
    SklA_AleId = models.ForeignKey(Alergeny, on_delete = models.CASCADE)
    SklA_SklId = models.ForeignKey(Skladniki, on_delete = models.CASCADE)

class KanapkiSkladniki(models.Model):
    KaS_Id = models.IntegerField(primary_key = True)
    KaS_SklId = models.ForeignKey(Skladniki, on_delete = models.CASCADE)
    KaS_KanId = models.ForeignKey(Kanapki, on_delete = models.CASCADE)
    Kas_Ilosc = models.IntegerField(null = True)
    Kas_Ilosc = models.IntegerField(null = True)