import React, { Component } from 'react';
import { Nav } from 'react-bootstrap';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Button from 'react-bootstrap/Button';
import CardDeck from 'react-bootstrap/CardDeck';
import Card from 'react-bootstrap/Card';
import Navigation from '../Components/Navigation';



class Home extends Component {
    render() {
      return (
        <div>
          <Navigation/>
        </div>
      );
    }
  }
  
  export default Home;
  