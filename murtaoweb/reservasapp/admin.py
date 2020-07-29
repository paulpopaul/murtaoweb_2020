from __future__ import unicode_literals
from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from .models import Reserva

import xlwt
# Register your models here.

def export_xls(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado-de-Reservas.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Reservas")

    row_num = 0

    columns = [
        # aquí los campos escritos en el Documento..
        (u"NOMBRE CONTACTO", 1999),
        (u"FECHA RESERVA", 2000),
        (u"HORA RESERVA", 2001),
        (u"NUMERO INVITADOS", 2002),
        (u"TELEFONO CONTACTO", 2003),
        (u"EMAIL CONTACTO", 2004),
        (u"MENSAJE", 2005),
        (u"REALIZADA", 2006),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in Reserva.objects.get_queryset():
        row_num += 1
        row = [
            # aquí los campos a exportar en excel
            obj.nombre_persona,
            obj.fecha_evento.isoformat(),
            obj.hora_evento.isoformat(),
            obj.numeros_invitados,
            obj.telefono_invitado,
            obj.email,
            obj.mensaje_evento,
            obj.reserva_realizada,
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

export_xls.short_description = u"Exportar XLS"


class ReservaAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Reserva'), {
            'fields': (('nombre_persona','reserva_realizada'), 'email', 'fecha_evento',
                       'hora_evento','numeros_invitados','telefono_invitado',
                       'mensaje_evento')})
        ,)
    search_fields = ('nombre_persona', 'fecha_evento', 'hora_evento', 'email')
    list_filter = ('nombre_persona', 'fecha_evento','reserva_realizada')
    list_display = ('nombre_persona','fecha_evento', 'hora_evento', 'reserva_realizada', 'email')
    list_display_links = ['nombre_persona', 'fecha_evento', 'hora_evento', 'reserva_realizada', 'email']

    actions = [export_xls]

    class Meta:
        model = Reserva

admin.site.register(Reserva, ReservaAdmin)