import React, { useEffect, useState } from 'react';

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
    <div>
      <h1 style={{ padding: '20px', margin: '20px' }}>Train Details</h1>
      <hr />
      <div style={{ display: 'flex', flexWrap: 'wrap' }}>
        {trains.map((train) => (
          <div
            key={train.trainNumber}
            style={{
              border: '1px solid gray',
              borderRadius: '5px',
              padding: '10px',
              margin: '10px',
              width: '300px',
            }}
          >
            <h2>{train.trainName}</h2>
            <p>Train Number: {train.trainNumber}</p>
            <p>Delayed By: {train.delayedBy} minutes</p>
            <p>
              Departure Time: {train.departureTime.Hours}:
              {train.departureTime.Minutes}:{train.departureTime.Seconds}
            </p>
            <p>Price (AC): {train.price.AC}</p>
            <p>Price (Sleeper): {train.price.sleeper}</p>
            <p>Seats Available (AC): {train.seatsAvailable.AC}</p>
            <p>Seats Available (Sleeper): {train.seatsAvailable.sleeper}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TrainDetails;
