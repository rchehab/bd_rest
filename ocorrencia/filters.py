from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.contrib import admin


class SemestreFilter(admin.SimpleListFilter):
    title = _('semestre')
    parameter_name = 'data'

    def lookups(self, request, model_admin):
        return (
            ('1st', _('1º Semestre')),
            ('2nd', _('2º Semestre')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1st':
            return queryset.filter(data__month__lte=6)
        if self.value() == '2nd':
            return queryset.filter(data__month__gte=7)


class PeriodoFilter(admin.SimpleListFilter):
    title = _('período')
    parameter_name = 'hora'

    def lookups(self, request, model_admin):
        return (
            ('diurno', _('Diurno')),
            ('noturno', _('Noturno')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'diurno':
            return queryset.filter(hora__hour__gte=6, hora__hour__lte=17)
        if self.value() == 'noturno':
            return queryset.filter((Q(hora__hour__gte=18) & Q(hora__hour__lte=23)) |
                                   (Q(hora__hour__gte=0) & Q(hora__hour__lte=5)))