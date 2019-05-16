from django.db import models

class Alergeny(models.Model):
    Ale_Nazwa = models.TextField(null=True)
    Ale_Ikona = models.ImageField(blank=True, null=True, upload_to="alegreny/images/")

class Skladniki(models.Model):
    Skl_Grupa = models.IntegerField()
    Skl_Nazwa = models.TextField(null=True)
    Skl_Archiwalny = models.IntegerField(null=True)
    Skl_Kcal = models.IntegerField(null=True)
    Skl_GramNaPorcje = models.IntegerField(null=True)
    Skl_Cena = models.IntegerField(null=True)
    Skl_Ikona = models.ImageField(blank=True, null=True, upload_to="skladniki/images/")
	
class Kanapki(models.Model):
    Kan_Cena = models.FloatField(null=True)
    Kan_Archiwalny = models.IntegerField(null=True)
    Kan_Ikona =  models.ImageField(blank=True, null=True, upload_to="kanapki/images/")

class SkladnikiAlergeny(models.Model):
    SklA_AleId = models.ForeignKey(Alergeny, on_delete=models.CASCADE)
    SklA_SklId = models.ForeignKey(Skladniki, on_delete=models.CASCADE)

class KanapkiSkladniki(models.Model):
    KaS_SklId = models.ForeignKey(Skladniki, on_delete=models.CASCADE)
    KaS_KanId = models.ForeignKey(Kanapki, on_delete=models.CASCADE)
    KaS_Ilosc = models.IntegerField(null=True)