def analyze_trip(distance_km, duration_minutes):

    analysis = {
        "trip_category":None,
        "driving_level": None,
        "recommendations": []
    }

    if distance_km < 70:
        analysis["trip_category"] = "Short trip"

    elif distance_km < 250:
        analysis["trip_catgeory"] = "Medium trip"

    else:
        analysis["trip_category"] = "Long trip"

    if duration_minutes < 90:
        analysis["driving_level"] = "Easy"

    elif duration_minutes < 240:
        analysis["driving_level"] = "Moderate"

    else:
        analysis["driving_level"] = "Demanding"

    if distance_km >= 250 or duration_minutes >= 240:
        analysis["recommendations"].append(
            "Plan a rest stop during the journey."
        )

    if duration_minutes >= 360:
        analysis["recommendations"].append(
            "Consider splitting the journey into multiple stages."
        )

    if distance_km >= 500:
        analysis["recommendations"].append(
            "Check fuel availability before departure."
        )

    return analysis