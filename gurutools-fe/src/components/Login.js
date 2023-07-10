import React, { Component } from "react";
import logo from "../images/GuruToolsLogo_RenderForest.png"
import logo_o from "../images/GuruHotelLogoOriginal.png"
import {
  Container,
  Row,
  Col,
  Card,
  CardBody,
  Button,
  Form,
  FormGroup,
  Label,
  Input,
  Toast,
  ToastBody,
  ToastHeader,
  Navbar,
} from "reactstrap";




class Login extends Component {


render () {
  
  return (



    <Container>



      <Row>
        <Col style={{maxWidth:"40%", margin: "auto"}}>
        <img
          src={logo}
          width="400"
          className="img-thumbnail"
          style={{ margin: "auto", border:0, display: "block", marginTop: "10px", marginBottom: "10px" }}
    />
         <br></br>
         <center>
         <h2 style={{margin: "auto", border:0, display: "block", marginTop: "50px", marginBottom: "20px"}}>Inicio de sesión</h2>
         </center>
          <Card>
         
         
            <CardBody>
              <Form>
         
                <FormGroup className="pb-2 mr-sm-2 mb-sm-0">
         <Label for="exampleEmail" className="mr-sm-2">
                    Correo
                  </Label>
                  <Input
                    type="email"
                    name="email"
                    id="exampleEmail"
                    placeholder="correo@guruhotel.com"
                    
                  />
                </FormGroup>
                <FormGroup className="pb-2 mr-sm-2 mb-sm-0">
                  <Label for="examplePassword" className="mr-sm-2">
                    Contraseña
                  </Label>
                  <Input
                    type="password"
                    name="password"
                    id="examplePassword"
                    placeholder="Escribe aquí tu contraseña"
                    
                  />
                </FormGroup>
                
                <Button type="submit" color="primary" style={{margin: "auto", border:0, display: "block", marginTop: "10px", marginBottom: "20px"}}>
                  Login
                </Button>
              </Form>
              <button type="submit" color="primary" style={{margin: "auto", border:0, display: "block", marginTop: "10px", marginBottom: "20px"}} >Continuar</button>

            </CardBody>
          </Card>
              </Col>
              
      </Row>

   <Row>
<center>
<div style={{marginTop: "90px"}}>
 <p>Powered by</p> 
<img
src={logo_o}
style={{margin: "auto", border:0, width:"120px", height: "32px" }}
/>
</div>
</center>
       </Row>

       </Container>


        );

};
}


export default Login;
