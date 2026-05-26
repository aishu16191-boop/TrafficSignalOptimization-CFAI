import time

# Function for signal timing
def get_signal_time(vehicle_count):
    if vehicle_count > 20:
        return 60
    elif vehicle_count > 10:
        return 40
    else:
        return 20

# Vehicle count on roads
roads = {
    "Road 1": 25,
    "Road 2": 12,
    "Road 3": 7,
    "Road 4": 18
}

road_names = list(roads.keys())

# Traffic Signal Control
for current_road in road_names:

    print("\n====================================")

    for road in road_names:

        if road == current_road:

            vehicles = roads[road]
            green_time = get_signal_time(vehicles)

            print(f"{road} --> GREEN")
            print(f"Vehicle Count : {vehicles}")
            print(f"Green Signal Time : {green_time} seconds")

        else:
            print(f"{road} --> RED")

    time.sleep(2)

    print(f"{current_road} --> YELLOW")
    time.sleep(1)

print("\nTraffic Cycle Completed")