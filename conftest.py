from dotenv import load_dotenv
load_dotenv()  # carga .env (o el que definas en la variable ENV) a os.environ

import os

USER = os.getenv("SL_USER")
PASS = os.getenv("SL_PASS")
BASE_URL = os.getenv("BASE_URL")

# Validación rápida para fallar temprano si falta algo
assert USER and PASS, "Faltan credenciales (SL_USER o SL_PASS) en .env"
