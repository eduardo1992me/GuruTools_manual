import { useState } from "react";
import {
  Button,
  Form,
  FormGroup,
  Label,
  Col,
  Input,
  FormText,
  Row,
  Alert,
} from "reactstrap";
import axios from "axios";
import AltaHotelRelacion from "../components/AltaHotelRelacion";


function AltaHotel() {
  const handleClick = () => {
    console.log(state);
    registro_gen_1();
  };

  const [state, setState] = useState({
    pk: 0,
    name: "",
    category: "",
    country: "",
    state: "",
    address: "",
    url: "",
    url_exp: "",
    url_bbk: "",
    current_hotel_id: ""
  });

  const [showRelacionComponent, setShowRelacionComponent] = useState(false);
  const [successAlert, setSuccessAlert] = useState(false);
  const [errorAlert, setErrorAlert] = useState(false);

  /*
function componentDidMount() {
    if (this.props.test_insert) {
        const {pk, nombre, categoria, edad} = this.props.hotel;
        this.setState({pk, nombre, categoria, edad});
    }
}
*/

  const defaultIfEmpty = (value) => (value === "" ? "" : value);

  const onChange = (e) => {
    setState({ ...state, [e.target.name]: e.target.value });
  };

  const registro_gen_1 = (e) => {
    axios
      .post("http://localhost:8000/api/hotel/registro_general_gen_1/", state)
      .then((response) => {
        // Maneja la respuesta exitosa
        console.log("Hotel Guardado");
        console.log(response);
        let current_hotel_id = response.data["id"];
        
        console.log(current_hotel_id);
        setSuccessAlert(true);
        setState({...state, current_hotel_id: current_hotel_id})
        setShowRelacionComponent(true);
      })
      .catch((error) => {
        // Maneja los errores de la solicitud
        setErrorAlert(true);
        console.log(error);
      });
  };

  return (
    <div
      style={{
        display: "block",

        padding: 30,
      }}
    >
      <Form>
        {successAlert && (
          <Alert color="success">Registro Gurdado correctamente</Alert>
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
              <Label for="hotelName">Nombre de hotel:</Label>
              <Input
                id="hotelName"
                name="name"
                placeholder="Ingresa el nombre del hotel"
                type="text"
                onChange={onChange}
                value={defaultIfEmpty(state.name)}
              />
            </FormGroup>
          </Col>
          <Col md={6}>
            <FormGroup>
              <Label for="typeCategory">Categoría de hotel</Label>
              <Input
                id="typeCategory"
                name="category"
                type="select"
                onChange={onChange}
                value={defaultIfEmpty(state.category)}
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
        </Row>

        <Row>
          <Col md={6}>
            <FormGroup>
              <Label for="typeCountry" sm={2}>
                País:
              </Label>
              <Col>
                <Input
                  id="typeCountry"
                  name="country"
                  type="select"
                  onChange={onChange}
                  value={defaultIfEmpty(state.country)}
                >
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
                  name="state"
                  placeholder="Ingrese aquí el nombre del estado del hotel"
                  type="text"
                  onChange={onChange}
                  value={defaultIfEmpty(state.state)}
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
              name="address"
              placeholder="Ingrese aquí la dirección del hotel"
              type="text"
              onChange={onChange}
              value={defaultIfEmpty(state.address)}
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
              onChange={onChange}
              value={defaultIfEmpty(state.url)}
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
              onChange={onChange}
              value={defaultIfEmpty(state.url_exp)}
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
              onChange={onChange}
              value={defaultIfEmpty(state.url_bbk)}
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
            <Button
              onClick={registro_gen_1}
              color="primary"
              style={{
                margin: "auto",
                border: 0,
                display: "block",
                marginTop: "10px",
                marginBottom: "20px",
              }}
            >
              Continuar
            </Button>
          </Col>
        </FormGroup>
      </Form>
      {showRelacionComponent && <AltaHotelRelacion data={state.current_hotel_id}/>}
    </div>
  );
}

export default AltaHotel;
