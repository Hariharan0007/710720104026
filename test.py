import datetime

data = {
    "delayedBy": 1,
    "departureTime": {
        "Hours": 23,
        "Minutes": 55,
        "Seconds": 0
    },
    "price": {
        "AC": 675,
        "sleeper": 442
    },
    "seatsAvailable": {
        "AC": 5,
        "sleeper": 15
    },
    "trainName": "Funny Exp",
    "trainNumber": "2341"
}

# Get the current time
current_time = datetime.datetime.now()

# Convert current time to only hours and minutes for comparison
current_time = current_time.replace(second=0, microsecond=0)

# Get the departure time from the data
departure_hours = data["departureTime"]["Hours"]
departure_minutes = data["departureTime"]["Minutes"]

# Create a datetime object for the departure time
departure_time = current_time.replace(hour=departure_hours, minute=departure_minutes)

# Calculate the time difference between current time and departure time
time_difference = departure_time - current_time

# Check if the time difference is within 12 hours
if time_difference <= datetime.timedelta(hours=12):
    # Sort the data based on departure time
    sorted_data = sorted([data], key=lambda x: datetime.datetime.combine(
        current_time.date(), datetime.time(x["departureTime"]["Hours"], x["departureTime"]["Minutes"])))

    print(sorted_data)
else:
    print("Departure time is more than 12 hours from the current time.")
