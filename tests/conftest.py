# tests/conftest.py
from dotenv import load_dotenv
load_dotenv()  # carga .env en os.environ

import os
import pytest
from playwright.sync_api import Page, expect

BASE_URL = os.getenv("BASE_URL")
USER     = os.getenv("SL_USER")
PASS     = os.getenv("SL_PASS")

# Valida al arrancar: si falta algo, aborta la suite para no perder tiempo
assert BASE_URL and USER and PASS, "⚠️  Variables de entorno incompletas"

@pytest.fixture
def pagina_logueada(page: Page):
    """Devuelve una página ya autenticada en Saucedemo."""
    page.goto(BASE_URL)

    page.fill('[data-test="username"]', USER)
    page.fill('[data-test="password"]', PASS)
    page.click('[data-test="login-button"]')

    expect(page.get_by_text("Swag Labs")).to_be_visible()
    yield page                     # ← entrega la page al test

    # (Playwright cierra el navegador automáticamente al final)
