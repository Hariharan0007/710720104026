from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime, timedelta


# current_time = datetime.datetime.now()
# formatted_time = current_time.strftime("%H:%M:%S")



app = Flask(__name__)
CORS(app)
API_URL = 'http://104.211.219.98/train/trains'
BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODcxNjY5MjAsImNvbXBhbnlOYW1lIjoiNzEwNzIwMTA0MDI2IiwiY2xpZW50SUQiOiJkOTFlNjY1Ni05MjZkLTQwNDUtYjM3ZS03NzA5OWE4Y2E0ZmYiLCJvd25lck5hbWUiOiIiLCJvd25lckVtYWlsIjoiIiwicm9sbE5vIjoiNzEwNzIwMTA0MDI2In0.Tf3Qq-7DUYNdNmaN0vSbl2xNwVN8fFbN5aL0zgXtYZA'

@app.route('/', methods=['GET'])
def get_sorted_trains():
    headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}
    response = requests.get(API_URL, headers=headers)
    response.raise_for_status()

    trains = response.json()


    trains = sortTime(trains)

    sorted_trains = sortTrains(trains)

    return jsonify(sorted_trains)

def sortTime(trains):
    current_time = datetime.now()
    filtered_trains = []

    for train in trains:
        departure_time = timedelta(
            hours=int(train['departureTime']['Hours']),
            minutes=int(train['departureTime']['Minutes']),
            seconds=int(train['departureTime']['Seconds'])
        ) + timedelta(minutes=train['delayedBy'])

        time_difference = departure_time.total_seconds() - (current_time.hour * 3600 + current_time.minute * 60 + current_time.second)

        if 1800 <= time_difference <= 12 * 3600:
            filtered_trains.append(train)

    return filtered_trains

def sortTrains(trains):
    def sort_key(train):
        price = train['price']['sleeper']
        seats_available = train['seatsAvailable']['sleeper']
        departure_time = train['departureTime']
        delayed_by = train['delayedBy']
        return (price, -seats_available, -(departure_time['Hours'] * 3600 + departure_time['Minutes'] * 60 + departure_time['Seconds']) - delayed_by)

    sorted_trains = sorted(trains, key=sort_key)
    return sorted_trains





if __name__ == '__main__':
    app.run(debug=True)
