IDEAL_TEMP = 22  

spaces = {
    "Living Room": 20,
    "Bedroom": 23,
    "Kitchen": 21
}

print("=== Simple Reflex System ===")

for area, degree in spaces.items():
    if degree < IDEAL_TEMP:
        print(f"{area}: {degree}°C -> Heater ON")
    else:
        print(f"{area}: {degree}°C -> Heater OFF")

print("\n=== Model-Based Reflex System ===")

heater_status = {
    "Living Room": "OFF",
    "Bedroom": "OFF",
    "Kitchen": "OFF"
}

for area, degree in spaces.items():
    if degree < IDEAL_TEMP and heater_status[area] == "OFF":
        heater_status[area] = "ON"
        print(f"{area}: {degree}°C -> Heater turned ON")
    elif degree >= IDEAL_TEMP and heater_status[area] == "ON":
        heater_status[area] = "OFF"
        print(f"{area}: {degree}°C -> Heater turned OFF")
    else:
        print(f"{area}: {degree}°C -> No change (Heater already {heater_status[area]})")
