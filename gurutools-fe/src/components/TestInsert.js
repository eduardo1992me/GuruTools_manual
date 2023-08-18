import React, { useState } from "react";
import { Row, Col, FormGroup, Label, Form, Input, Button, Alert } from "reactstrap";
import axios from "axios";
import { API_URL } from "../constants";

function TestInsert() {
  const handleClick = () => {
    console.log(state);
    insertInfo()

  };

  const [state, setState] = useState({
    pk: 0,
    nombre: "",
    categoria: "",
    edad: "",
  });

  const [successAlert, setSuccessAlert] = useState(false);
  const [errorAlert, setErrorAlert] = useState(false);


  const defaultIfEmpty = (value) => (value === "" ? "" : value);

  const onChange = (e) => {
    setState({ ...state, [e.target.name]: e.target.value });
  };

  const insertInfo = (e) => {
    axios.post('http://localhost:8000/api/hotel/test_registro/', state)
        .then(response => {
            // Maneja la respuesta exitosa
            console.log("Guardado Cor")
            setSuccessAlert(true);

        })
          .catch(error => {
            // Maneja los errores de la solicitud
            setErrorAlert(true)
            console.log(error);
          });
  };

  return (
    <div style={{ margin: "20px" }}>
      <Form>
      {successAlert && (
          <Alert color="success">
            Registro Gurdado correctamente
          </Alert>
        )}

        {/* Renderizar la alerta de error */}
        {errorAlert && (
          <Alert color="danger">
            El registro no se guardo de forma correcta
          </Alert>
        )}
        <Row>
          <Col md={6}>
            <FormGroup>
              <Label for="name">Nombre :</Label>
              <Input
                id="name"
                name="nombre"
                placeholder="Ingresa el nombre"
                type="text"
                onChange={onChange}
                value={defaultIfEmpty(state.nombre)}
              />
            </FormGroup>
          </Col>
          <Col md={6}>
            <FormGroup>
              <Label for="typecategory">Categoría de hotel</Label>
              <Input
                id="typecategory"
                name="categoria"
                type="select"
                onChange={onChange}
                value={defaultIfEmpty(state.categoria)}
              >
                <option>Business Class</option>
                <option>Boutique</option>
                <option>B&B</option>
                <option>Resort</option>
                <option>Posada</option>
                <option>Bungalow</option>
              </Input>
            </FormGroup>
          </Col>

          <Col md={6}>
            <FormGroup>
              <Label for="age">Edad</Label>
              <Input
                id="age"
                name="edad"
                type="number"
                onChange={onChange}
                value={defaultIfEmpty(state.edad)}
              ></Input>
            </FormGroup>
          </Col>
        </Row>
        <br></br>

        <Button onClick={insertInfo}>Guardar</Button>
      </Form>
    </div>
  );
}

export default TestInsert;
