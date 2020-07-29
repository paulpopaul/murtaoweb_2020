from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.http import HttpResponse

from .models import SuscripcionUsuario, Suscripcion

import xlwt

# Register your models here.

def export_xls(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado-de-Mail.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("BASE DATOS MAIL")

    row_num = 0

    columns = [
        # aquí los campos escritos en el Documento..
        (u"NUMERO_ID", 1998),
        (u"NOMBRE", 1999),
        (u"APELLIDO", 2001),
        (u"TELEFONO", 2002),
        (u"EMAIL", 2003),
        (u"F_NACIMIENTO", 2004),
        (u"CIUDAD", 2005),
        (u"FECHA INGRESO", 2006),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in SuscripcionUsuario.objects.get_queryset():
        row_num += 1
        row = [
            # aquí los campos a exportar en excel
            obj.numero_id,
            obj.nombre,
            obj.apellido,
            obj.telefono,
            obj.email,
            obj.f_nacimiento.isoformat(),
            obj.ciudad,
            obj.fecha_ingreso.isoformat(),
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

export_xls.short_description = u"Exportar XLS"

class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ('numero_id', 'nombre', 'apellido', 'email', 'f_nacimiento', 'ciudad', 'fecha_ingreso')
    list_filter = ('email', 'f_nacimiento', 'fecha_ingreso')
    search_fields = ('email', 'f_nacimiento', 'fecha_ingreso')

    actions = [export_xls]

    class Meta:
        model = SuscripcionUsuario

admin.site.register(SuscripcionUsuario, SuscripcionAdmin)
admin.site.register(Suscripcion)


