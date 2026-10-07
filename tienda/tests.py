from decimal import Decimal
from types import SimpleNamespace

from django.contrib import admin
from django.test import TestCase

from tienda.admin import PedidoAdmin
from tienda.models import Pedido


class PedidoAdminTests(TestCase):
	def test_total_formateado_usa_puntos_de_millar_y_signo_peso(self):
		pedido = SimpleNamespace(total=Decimal('1000000.00'))
		pedido_admin = PedidoAdmin(Pedido, admin.site)

		self.assertEqual(pedido_admin.total_formateado(pedido), '$1.000.000')
