import requests
from config import NOMINATIM_URL, HEADERS, REQUEST_TIMEOUT
from utils.logger import logger

MIN_IMPORTANCE = 0.1


def get_address(prompt):
    address = input(prompt)
    logger.info(f"Searching location: {address}")

    params = {
    "q": address,
    "format": "json",
    "limit": 1,
    "addressdetails": 1
    }

    try:
        response = requests.get(
            url=NOMINATIM_URL, params=params, headers=HEADERS, timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()

    except requests.exceptions.Timeout:
        logger.error(f"Geocoding timed out for '{address}'")
        print("Geocoding timed out.")
        return None

    except requests.exceptions.ConnectionError:
        logger.error(f"No internet connection while geocoding '{address}'")
        print("No internet connection.")
        return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Geocoding request failed for '{address}': {e}")
        print("Geocoding request failed.")
        return None

    try:
        result = response.json()

        if not result:
            print("Unable to locate this address.Please provide a more specific location.")
            logger.warning(f"Location not found: {address}")
            return None

        place = result[0]
        importance = float(place.get("importance", 0))

        if importance < MIN_IMPORTANCE:
            print("Location is unclear. Please enter a more specific place.")
            logger.warning(f"Low-confidence match for '{address}' (importance={importance})")
            return None

        latitude = float(place["lat"])
        longitude = float(place["lon"])

        logger.info(f"Confirmed location: {address}")

        return {
            "name": address,
            "coordinates": [latitude, longitude]
        }

    except (ValueError, KeyError, IndexError) as e:
        logger.error(f"Invalid geocoding response for '{address}': {e}")
        print("Invalid location data received.")
        return None
