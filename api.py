from flask import Flask, jsonify
import requests
import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
print(formatted_time)


app = Flask(__name__)
API_URL = 'http://104.211.219.98/train/trains'
BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODcxNTcyNTksImNvbXBhbnlOYW1lIjoiNzEwNzIwMTA0MDI2IiwiY2xpZW50SUQiOiJkOTFlNjY1Ni05MjZkLTQwNDUtYjM3ZS03NzA5OWE4Y2E0ZmYiLCJvd25lck5hbWUiOiIiLCJvd25lckVtYWlsIjoiIiwicm9sbE5vIjoiNzEwNzIwMTA0MDI2In0.fJ14yqH3VJCu29-xg8-_mn1ykmeohUPbI7tx8CAd2X0'

@app.route('/', methods=['GET'])
def get_sorted_trains():
    headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}
    response = requests.get(API_URL, headers=headers)
    response.raise_for_status()

    # data = response.json()

    data =[
  {
    "delayedBy": 1,
    "departureTime": {
      "Hours": 0,
      "Minutes": 10,
      "Seconds": 0
    },
    "price": {
      "AC": 645,
      "sleeper": 412
    },
    "seatsAvailable": {
      "AC": 5,
      "sleeper": 15
    },
    "trainName": "Funny Exp",
    "trainNumber": "2341"
  },
  {
    "delayedBy": 1,
    "departureTime": {
      "Hours": 15,
      "Minutes": 15,
      "Seconds": 0
    },
    "price": {
      "AC": 645,
      "sleeper": 412
    },
    "seatsAvailable": {
      "AC": 5,
      "sleeper": 15
    },
    "trainName": "Funny Exp",
    "trainNumber": "2341"
  }
    ]

    selected_train = []
    
    for train in data:
        departure_hours = train["departureTime"]["Hours"]
        departure_minutes = train["departureTime"]["Minutes"]

        departure_time = current_time.replace(hour=departure_hours, minute=departure_minutes)

        time_difference = departure_time - current_time

        print(time_difference)

        if time_difference <= datetime.timedelta(hours=12):
            selected_train.append(train)
        else:
            print("Departure time is more than 12 hours from the current time.")

    

    return jsonify(selected_train)

if __name__ == '__main__':
    app.run(debug=True)
