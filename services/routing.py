import requests
from config import GRAPHHOPPER_URL, GRAPHHOPPER_API_KEY, REQUEST_TIMEOUT, HEADERS
from utils.logger import logger


def route(locations):
    points = []

    params = [
    ("profile", "car"),
    ("locale", "en"),
    ("calc_points", "true"),
    ("key", GRAPHHOPPER_API_KEY)
]

    for location in locations:
        lat, lon = location["coordinates"]
        params.append(
        ("point", f"{lat},{lon}")
    )

    try:
        logger.info("Requesting route from GraphHopper")

        response = requests.get(
            url=GRAPHHOPPER_URL, params=params, headers=HEADERS, timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()

    except requests.exceptions.Timeout:
        logger.error("Routing request timed out")
        print("Routing server timed out.")
        return None

    except requests.exceptions.ConnectionError:
        logger.error("No internet connection while routing")
        print("No internet connection.")
        return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Routing request failed: {e}")
        print("Routing request failed.")
        return None

    try:
        result = response.json()

        if "paths" not in result:
            logger.error(f"GraphHopper error response: {result}")
            print("GraphHopper could not create a route.")
            return None

        path = result["paths"][0]

    except ValueError:
        logger.error("Invalid JSON received from GraphHopper")
        print("Invalid server response.")
        return None

    minutes = round(path["time"] / 1000 / 60)
    hours = minutes // 60
    mins = minutes % 60

    route_data = {
        "Distance-km": f'{round(path["distance"] / 1000, 2)} km',
        "Time-mins": f'{hours} hours {mins} minutes',
        "steps": []
    }

    for step in path["instructions"]:
        step_minutes = round(step["time"] / 1000 / 60)
        route_data["steps"].append({
            "instruction": step["text"],
            "distance": f'{round(step["distance"], 2)} m',
            "time": f'{step_minutes} minutes'
        })

    logger.info("Route calculated successfully")
    return route_data
