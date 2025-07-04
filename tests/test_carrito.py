# tests/test_carrito.py
from playwright.sync_api import expect

def test_agregar_producto(pagina_logueada):
    # 1) La página YA está logueada
    pagina_logueada.click(".inventory_item:first-child button")

    # 2) Verifico que el carrito marque “1”
    expect(pagina_logueada.locator(".shopping_cart_badge")).to_have_text("1")
