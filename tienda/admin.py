from django.contrib import admin
from tienda.models import Cliente
from tienda.models import Pedido

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo', 'telefono', 'direccion']
    list_filter = ['nombre']
    search_fields = ['nombre', 'correo', 'telefono']

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'nombre_producto', 'cantidad', 'fecha', 'total_formateado', 'entregado']
    list_filter = ['entregado', 'fecha']
    search_fields = ['cliente__nombre', 'cliente__correo']

    @admin.display(description='Total', ordering='total')
    def total_formateado(self, pedido):
        return f"${pedido.total:,.0f}".replace(',', '.')

# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)