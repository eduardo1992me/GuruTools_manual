import React, { Component } from "react";
import logo from "../images/GuruToolsLogo_RenderForest.png"
import 'bootstrap/dist/css/bootstrap.min.css';
import {
    Navbar,
    NavItem,
    NavbarToggler,
    Collapse,
    NavLink,
    Nav,
    NavbarBrand,
    Container,
    Row
} from 'reactstrap';


class Header extends Component {
  render() {
    return (
        <div className="text-left">

          

          <Navbar color="white" light expand="md">
                    <NavbarBrand> 
                    <img
                src={logo}
                width="300"
                className="img-thumbnail"
                style={{ marginTop: "15px", marginLeft: "10px", border:0, display: "block" }}
          />

                    </NavbarBrand>
                    
                        <Nav className="ml-auto" navbar style={{marginRight: "80px", fontSize:"20px"}}>
                            <NavItem>
                                <NavLink href="#">Hoteles</NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink href="#">Monitoreos del día</NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink href="#">Reportes</NavLink>
                            </NavItem>
                        </Nav>
                       
                </Navbar>

          
        </div>
        

        
       
      );
    }
  }
  
  export default Header;