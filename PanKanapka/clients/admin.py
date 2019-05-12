from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Uzytkownik, Organizacja


class ClientAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'imie', 'grupa', 'nazwisko', 'aktywny', 'obsluga')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'imie', 'grupa', 'nazwisko', 'aktywny', 'obsluga')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'grupa', 'password1', 'password2', 'imie', 'nazwisko', 'aktywny', 'obsluga')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Uzytkownik, ClientAdmin)
admin.site.register(Organizacja)
