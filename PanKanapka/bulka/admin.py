from django.contrib import admin
from .models import Alergeny, Skladniki, Kanapki, SkladnikiAlergeny, KanapkiSkladniki

admin.site.register(Alergeny)
admin.site.register(Skladniki)
admin.site.register(Kanapki)
admin.site.register(SkladnikiAlergeny)
admin.site.register(KanapkiSkladniki)
