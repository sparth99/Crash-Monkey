import React from 'react';
import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { Route, BrowserRouter } from 'react-router-dom';
import Home from './Pages/Home.js';
import Containers from './Pages/Containers.js'




function App() {
  return (
    <div className="App">
        <BrowserRouter>
          <Route exact path="/" component={Home} />
          <Route path={"/containers"} component={Containers}/>
        </BrowserRouter>
      </div>
  );
}

export default App;
