import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import trainImage from './train.png';

const TrainDetails = () => {
  const [trains, setTrains] = useState([]);

  useEffect(() => {
    fetchTrains();
  }, []);

  const fetchTrains = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/');
      const data = await response.json();
      setTrains(data);
    } catch (error) {
      console.log('Error fetching trains:', error);
    }
  };

  return (
    <div className="container">
      <h1 className="mt-5 mb-4">Train Details</h1>
      <hr />
      <div className="row">
        {trains.map((train) => (
          <div
            key={train.trainNumber}
            className="col-md-4 mb-4"
          >
            <div className="card h-100">
            <img src={trainImage} className="card-img-top" alt="Train" />
              <div className="card-body">
                <h5 className="card-title">{train.trainName}</h5>
                <p className="card-text">Train Number: {train.trainNumber}</p>
                <p className="card-text">Delayed By: {train.delayedBy} minutes</p>
                <p className="card-text">Departure Time: {train.departureTime.Hours}:{train.departureTime.Minutes}:{train.departureTime.Seconds}</p>
                <p className="card-text">Price (AC): {train.price.AC}</p>
                <p className="card-text">Price (Sleeper): {train.price.sleeper}</p>
                <p className="card-text">Seats Available (AC): {train.seatsAvailable.AC}</p>
                <p className="card-text">Seats Available (Sleeper): {train.seatsAvailable.sleeper}</p>
                <button className="btn btn-primary">Go to Train</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TrainDetails;
