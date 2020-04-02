import React, { Component } from 'react';
import Button from 'react-bootstrap/Button';
import CardDeck from 'react-bootstrap/CardDeck';
import Card from 'react-bootstrap/Card';
import Navigation from '../Components/Navigation';



class Home extends Component {
    render() {
      return (
        <div>
            <Navigation/>
            <h1>Containers</h1>
            <CardDeck>
                <Card border="primary" style={{ width: '18rem' }}>
                <Card.Header as="h5">lucid_turing</Card.Header>
                <Card.Body>
                    <Card.Title>ID: XHJ783JK</Card.Title>
                    <Card.Text>
                    With supporting text below as a natural lead-in to additional content.
                    </Card.Text>
                    <Button variant="primary">Tests</Button>
                </Card.Body>
                </Card>

                <Card border="primary" style={{ width: '18rem' }}>
                <Card.Header as="h5">lucid_turing</Card.Header>
                <Card.Body>
                    <Card.Title>ID: XHJ783JK</Card.Title>
                    <Card.Text>
                    With supporting text below as a natural lead-in to additional content.
                    </Card.Text>
                    <Button variant="primary">Tests</Button>
                </Card.Body>
                </Card>

                <Card border="primary" style={{ width: '18rem' }}>
                <Card.Header as="h5">lucid_turing</Card.Header>
                <Card.Body>
                    <Card.Title>ID: XHJ783JK</Card.Title>
                    <Card.Text>
                    With supporting text below as a natural lead-in to additional content.
                    </Card.Text>
                    <Button variant="primary">Tests</Button>
                </Card.Body>
                </Card>
                
            </CardDeck>
        </div>
      );
    }
  }
  
  export default Home;
  