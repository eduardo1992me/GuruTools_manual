import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import {
    Navbar,
    NavItem,
    NavbarToggler,
    Collapse,
    NavLink,
    Nav,
    NavbarBrand
} from 'reactstrap';

class NavBarMain extends Component {   
    render() {
       // const [isOpen, setIsOpen] = React.useState(false);
        return (
            <center>
            <div style={{
                display: 'block', width: 400, padding: 30
            }}>
                
                <Navbar color="light" light expand="md">
                    <NavbarBrand href="/">Inicio</NavbarBrand>
                    <NavbarToggler />
                    <Collapse navbar>
                        <Nav className="mr-auto" navbar>
                            <NavItem>
                                <NavLink href="#">Alta de Hotel</NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink href="#">Reportes</NavLink>
                            </NavItem>
                        </Nav>
                    </Collapse>
                </Navbar>
                
            </div >
            </center>
        );
        }
    }

    export default NavBarMain;