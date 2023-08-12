import React from "react";
import { Button, Form, FormGroup, Label, Col, Input, FormText, Row } from "reactstrap";

function AltaHotel() {
  return (
    <div style={{
        display: "block",
        
        padding: 30
      }}>
    <Form >

    <Row>
    <Col md={6}>
      <FormGroup>
        <Label for="hotelName">
          Nombre de hotel:
        </Label>
        <Input
          id="hotelName"
          name="name"
          placeholder="Ingresa el nombre del hotel"
          type="text"
        />
      </FormGroup>
    </Col>
    <Col md={6}>
      <FormGroup>
        <Label for="typeCategory">
          Categoría de hotel
        </Label>
        <Input id="typeCategory" name="select" type="select">
            <option>Business Class</option>
            <option>Boutique</option>
            <option>B&B</option>
            <option>Resort</option>
            <option>Posada</option>
            <option>Bungalow</option>
          </Input>
      </FormGroup>
    </Col>
  </Row>
  

  <Row>
    <Col md={6}>
      <FormGroup>
      <Label for="typeCountry" sm={2}>
          País:
        </Label>
        <Col>
          <Input id="typeCountry" name="select" type="select">
            <option>México</option>
            <option>Estados Unidos</option>
            <option>Colombia</option>
            <option>Puerto Rico</option>
            <option>Perú</option>
            <option>Argentina</option>
          </Input>
          </Col>
      </FormGroup>
    </Col>
    <Col md={6}>
      <FormGroup>
      <Label for="stateName" sm={2}>
        Estado/Provincia:
        </Label>
        <Col>
          <Input
            id="stateName"
            name="estado"
            placeholder="Ingrese aquí el nombre del estado del hotel"
            type="text"
          />
        </Col>
      </FormGroup>
    </Col>
  </Row>


      <FormGroup row>
        <Label for="hotelAddress" sm={2}>
        Dirección:
        </Label>
        <Col sm={10}>
          <Input
            id="hotelAddress"
            name="direccion"
            placeholder="Ingrese aquí la dirección del hotel"
            type="text"
          />
        </Col>
      </FormGroup>
      <FormGroup row>
        <Label for="urlHotel" sm={2}>
        URL del sitio web:
        </Label>
        <Col sm={10}>
          <Input
            id="urlHotel"
            name="url"
            placeholder="ej: https://www.maglenresort.com"
            type="text"
          />
        </Col>
      </FormGroup>

      <FormGroup row>
        <Label for="urlExpedia" sm={2}>
        URL de Expedia del hotel:
        </Label>
        <Col sm={10}>
          <Input
            id="urlExpedia"
            name="url_exp"
            placeholder="ej: https://www.expedia.com/maglen-resort..."
            type="text"
          />
        </Col>
      </FormGroup>

      <FormGroup row>
        <Label for="urlBooking" sm={2}>
        URL de Booking del hotel:
        </Label>
        <Col sm={10}>
          <Input
            id="urlBooking"
            name="url_bbk"
            placeholder="ej: https://www.booking.com/maglen-resort..."
            type="text"
          />
        </Col>
      </FormGroup>
      
     
      <FormGroup row>
        <Label for="checkbox2" sm={2}>
          Estado del hotel
        </Label>
        <Col
          sm={{
            size: 10,
          }}
        >
          <FormGroup check>
            <Input id="checkbox2" type="checkbox" checked />{" "}
            <Label check>Activo</Label>
          </FormGroup>
        </Col>
      </FormGroup>
      <FormGroup check row>
        <Col
          sm={{
            offset: 1,
            size: 10,
          }}
          
        >
            
          <Button type="submit" color="primary" style={{margin: "auto", border:0, display: "block", marginTop: "10px", marginBottom: "20px"}} >Continuar</Button>
          </Col>
        
      </FormGroup>
    </Form>
    </div>
  );
}

export default AltaHotel;
