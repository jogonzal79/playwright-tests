import re
from playwright.sync_api import Page, expect


def test_verificar_entorno(page: Page):
    """
    Smoke test: comprueba que Playwright, Pytest y el entorno funcionan.
    """
    # ARRANGE & ACT
    page.goto("https://playwright.dev/python/")

    # ASSERT: el título contiene "Playwright Python"
    expect(page).to_have_title(re.compile(r"Playwright Python"))
