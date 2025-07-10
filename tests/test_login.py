from playwright.sync_api import Page, expect


def test_login_exitoso(page: Page):
    # ARRANGE & ACT
    page.goto("https://www.saucedemo.com/")
    
    # ASSERT: Login en "Swag Labs"
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    
     # ASSERT: Verificar que estamos en el inventario
     #expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Swag Labs")).to_be_visible()

    # ---------------------
#Jonathan Gonzalez
# Este test verifica que el login en "Swag Labs" funcione correctamente.