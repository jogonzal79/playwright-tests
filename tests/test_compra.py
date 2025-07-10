# tests/test_compra.py
from playwright.sync_api import expect


def test_compra_completa(pagina_logueada):
    """
    Flujo end-to-end:
    1. El usuario ya está logueado (lo hace el fixture).
    2. Añade un producto al carrito.
    3. Finaliza la compra llenando el formulario.
    4. Verifica que la compra haya sido exitosa.
    """

    # 1) Añadir producto al carrito
    pagina_logueada.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    pagina_logueada.click('[data-test="shopping-cart-link"]')

    # 2) Proceder al checkout
    pagina_logueada.click('[data-test="checkout"]')

    # 3) Llenar formulario de envío
    pagina_logueada.fill('[data-test="firstName"]', "Jonathan")
    pagina_logueada.fill('[data-test="lastName"]', "Gonzalez")
    pagina_logueada.fill('[data-test="postalCode"]', "1010")
    pagina_logueada.click('[data-test="continue"]')

    # 4) Finalizar la compra
    pagina_logueada.click('[data-test="finish"]')

    # 5) Verificar mensaje de confirmación
    expect(pagina_logueada.locator('[data-test="complete-header"]')).to_have_text(
        "Thank you for your order!"
    )
#Jonathan Gonzalez
# Este test cubre el flujo completo de compra, desde añadir un producto hasta confirmar la orden