import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import TrainDetails from './TrainDetails';
import TrainDetailsPage from './TrainDetailsPage';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={TrainDetails} />
        <Route path="/train/:trainNumber" component={TrainDetailsPage} />
      </Switch>
    </Router>
  );
}

export default App;
