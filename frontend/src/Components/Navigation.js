import React from 'react';
import { Nav, Navbar, Form, FormControl, Button, NavDropdown } from 'react-bootstrap';


class Navigation extends React.Component {
  render() {
    return (
      <>
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
    <Navbar.Brand href="#home">Crash Monkey</Navbar.Brand>
    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
    <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="mr-auto">
        <Nav.Link href="#features">Reports</Nav.Link>
        <Nav.Link href="#pricing">Containers</Nav.Link>
        <NavDropdown title="Tests" id="collasible-nav-dropdown">
            <NavDropdown.Item href="#action/3.1">CPU</NavDropdown.Item>
            <NavDropdown.Item href="#action/3.2">Memory</NavDropdown.Item>
            <NavDropdown.Item href="#action/3.3">Network</NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item href="#action/3.4"><Button variant="outline-primary">Run Test</Button></NavDropdown.Item>
        </NavDropdown>
        </Nav>
    </Navbar.Collapse>
    </Navbar>

    
      </>
    );
  }
}

export default Navigation;
