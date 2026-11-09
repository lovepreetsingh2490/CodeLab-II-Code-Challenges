def collect_user_data():
    """Collect monthly car and electricity usage."""
    car_miles = float(input("Enter monthly car miles travelled: "))
    electricity_kwh = float(input("Enter monthly electricity usage (kWh): "))

    return car_miles, electricity_kwh


def calculate_emissions(car_miles, electricity_kwh):
    """Calculate total monthly carbon emissions."""
    total = (car_miles * 0.25) + (electricity_kwh * 0.20)
    return total


def classify_emissions(total):
    """Classify emissions based on the total."""
    if total < 100:
        return "Low"
    elif total <= 300:
        return "Moderate"
    else:
        return "High"


if __name__ == "__main__":
    print("=== Carbon Footprint Calculator ===")

    car_miles, electricity_kwh = collect_user_data()

    total = calculate_emissions(car_miles, electricity_kwh)
    classification = classify_emissions(total)

    print("\n=== Monthly Carbon Report ===")
    print(f"Total Emissions: {total:.2f}")
    print(f"Classification: {classification}")

