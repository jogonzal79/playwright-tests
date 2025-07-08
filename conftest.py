from dotenv import load_dotenv
load_dotenv()  # carga .env (o el que definas en la variable ENV) a os.environ

import os

USER = os.getenv("SL_USER")
PASS = os.getenv("SL_PASS")
BASE_URL = os.getenv("BASE_URL")

# Validación rápida para fallar temprano si falta algo
assert USER and PASS, "Faltan credenciales (SL_USER o SL_PASS) en .env"

# Configuración de pytest para generar reportes HTML con timestamp
# y guardarlos en un directorio específico.
import datetime
import os
import pytest

def pytest_configure(config):
    """Si el plugin pytest-html está activo, añade timestamp al nombre."""
    if config.pluginmanager.hasplugin("html"):
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_dir = "reports"
        os.makedirs(report_dir, exist_ok=True)
        config.option.htmlpath = os.path.join(report_dir, f"report_{ts}.html")
