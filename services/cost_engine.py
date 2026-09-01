def calculate_fuel_cost(distance_km, consumption, fuel_price):
    fuel_used = (distance_km / 100) * consumption
    cost = fuel_used * fuel_price

    return {
        "fuel_used": round(fuel_used, 2),
        "fuel_cost": round(cost, 2)
    }