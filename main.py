from services import geo_coding
from services import routing
from services import cost_engine
from core import trip_analyzer

def collect_locations():
    locations = []

    while True:
        start = geo_coding.get_address("Where are you leaving from?: ")
        if start:
            locations.append(start)
            break
        print("Location not recognized.")

    while True:
        try:
            print('\nYou can create a route with multiple locations.\n')
            destinations = int(input("Add your stops: "))
            if destinations < 1:
                print("A route needs at least 1 stop. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(destinations):
        while True:
            destination = geo_coding.get_address(
                f"Stop {i + 1} \n location: "
            )
            if destination:
                locations.append(destination)
                break
            print("Stop location not recognized.")

    return locations

def print_route(result,trip_cost,trip_analysis):
    print("\nROUTE OVERVIEW")
    print("----------------")
    print("Category:", trip_analysis["trip_category"])
    print("Driving level:", trip_analysis["driving_level"])
    print("Total Distance:", result["Distance-km"])
    print("Estimated Time:", result["Time-mins"])
    print("Fuel Used:", trip_cost["fuel_used"], "L")
    print("Fuel Cost:", trip_cost["fuel_cost"])
    print("----------------")

    if trip_analysis["recommendations"]:
        print("\nRecommendations:")

        for item in trip_analysis["recommendations"]:
            print("-", item)

    ask = input("\nBegin navigation? (y/n):  ")

    if ask.lower() == "y":
        for i, step in enumerate(result["steps"], start=1):
            print(f"\nStep {i}:")
            print(step["instruction"])
    else:
        print("Navigation cancelled.")


def main():
    print("""
    =================================
         Better Drive Assistant
         Route Planning System
    =================================
    """)

    print("Preparing route calculation...\n")
    locations = collect_locations()

    print("\nProcessing your route...\n")
    result = routing.route(locations)

    if result is None:
        print("Unable to calculate route\nPlease try again.")
        return

    distance = float(
    result["Distance-km"].replace(" km", "")
    )

    duration_text = result["Time-mins"]

    duration_minutes = 0

    if "hours" in duration_text:
        hours = int(duration_text.split(" hours")[0])
        minutes = int(duration_text.split("hours ")[1].replace(" minutes", ""))
        duration_minutes = hours * 60 + minutes

    else:
        duration_minutes = int(
        duration_text.replace(" minutes", "")
    )


    trip_analysis = trip_analyzer.analyze_trip(
        distance,
        duration_minutes
    )

    print('Route successfully calculated.')

    distance = distance

    consumption = float(
        input("\nVehicle fuel consumption  (L/100km): ")
    )

    fuel_price = float(
        input("Fuel price per liter: ")
    )

    trip_cost = cost_engine.calculate_fuel_cost(
        distance,
        consumption,
        fuel_price
    )

    print_route(result, trip_cost,trip_analysis)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
