from django.db import models


class Alergeny(models.Model):
    Ale_Nazwa = models.TextField(null=True)
    Ale_Ikona = models.BinaryField(null=True)

    def __str__(self):
        return self.Ale_Nazwa


class Skladniki(models.Model):
    Skl_Grupa = models.IntegerField()
    Skl_Nazwa = models.TextField(null=True)
    Skl_Archiwalny = models.IntegerField(null=True)
    Skl_Kcal = models.IntegerField(null=True)
    Skl_GramNaPorcje = models.IntegerField(null=True)
    Skl_Cena = models.IntegerField(null=True)
    Skl_Ikona = models.BinaryField(null=True)

    def __str__(self):
        return self.Skl_Nazwa


class Kanapki(models.Model):
    Kan_Nazwa = models.TextField(null=True)
    Kan_Cena = models.FloatField(null=True)
    Kan_Archiwalny = models.IntegerField(null=True)
    Kan_Ikona = models.BinaryField(null=True)

    def __str__(self):
        return self.Kan_Nazwa or 'nowa kanapka nr {}'.format(self.pk)


class SkladnikiAlergeny(models.Model):
    SklA_AleId = models.ForeignKey(Alergeny, on_delete=models.CASCADE)
    SklA_SklId = models.ForeignKey(Skladniki, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class KanapkiSkladniki(models.Model):
    KaS_SklId = models.ForeignKey(Skladniki, on_delete=models.CASCADE)
    KaS_KanId = models.ForeignKey(Kanapki, on_delete=models.CASCADE)
    KaS_Ilosc = models.IntegerField(null=True)

    def __str__(self):
        return str(self.pk)
