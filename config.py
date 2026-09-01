import os
from dotenv import load_dotenv

load_dotenv()

GRAPHHOPPER_URL = "https://graphhopper.com/api/1/route"
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

REQUEST_TIMEOUT = 10

HEADERS = {
    "User-Agent": "better-drive-assistant/1.0 (contact: Mohammadd.hasani.dev@gmail.com)"
}

GRAPHHOPPER_API_KEY = os.getenv("GRAPHHOPPER_API_KEY")

if not GRAPHHOPPER_API_KEY:
    raise RuntimeError(
        "GRAPHHOPPER_API_KEY is missing."
    )
