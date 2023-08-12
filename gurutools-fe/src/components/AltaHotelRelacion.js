import { useState } from "react";
import {
  Table,
  Col,
  Button,
  Modal,
  ModalBody,
  ModalFooter,
  ModalHeader,
  Input,
  Label,
  FormGroup,
  Tooltip,
  UncontrolledTooltip,
} from "reactstrap";
import { DatePicker } from "@guruhotel/aura-ui";
import CalendarT from "./CalendarT";

function AltaHotelRelacion(args) {
  const [modal, setModal] = useState(false);
  const toggle = () => setModal(!modal);

  return (
    <div
      style={{
        display: "block",

        padding: 30,
      }}
    >
      <h1>Maglen Resort</h1>
      <br></br>
      <h4>Relación de habitaciones</h4>
      <Table bordered hover responsive size="" striped>
        <thead>
          <tr>
            <th>#</th>
            <th>Guruhotel</th>
            <th>Expedia</th>
            <th>Booking</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>Sencilla, 1 cama king size</td>
            <td>
              <Input id="selectCategory" name="select" type="select">
                <option>Basica, 2 personas</option>
                <option>Doble, 4 personas</option>
                <option>Luxury Room Romance, 2 personas</option>
              </Input>
            </td>
            <td>
              <Input id="selectCategory" name="select" type="select">
                <option>Sencilla King</option>
                <option>Habitación doble</option>
                <option>Habitación Luxury</option>
              </Input>
            </td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Doble, 2 camas matrimoniales</td>
            <td>
              <Input id="selectCategory" name="select" type="select">
                <option>Basica, 2 personas</option>
                <option>Doble, 4 personas</option>
                <option>Luxury Room Romance, 2 personas</option>
              </Input>
            </td>
            <td>
              <Input id="selectCategory" name="select" type="select">
                <option>Sencilla King</option>
                <option>Habitación doble</option>
                <option>Habitación Luxury</option>
              </Input>
            </td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td>Penthouse, 1 cama King Size</td>
            <td>
              <Input id="selectCategory" name="select" type="select">
                <option>Basica, 2 personas</option>
                <option>Doble, 4 personas</option>
                <option>Luxury Room Romance, 2 personas</option>
              </Input>
            </td>
            <td>
              <Input id="selectCategory" name="select" type="select">
                <option>Sencilla King</option>
                <option>Habitación doble</option>
                <option>Habitación Luxury</option>
              </Input>
            </td>
          </tr>
        </tbody>
      </Table>
      <br></br>
      <form>


       <div>
        <h4 style={{
              display: "inline-block", marginRight: "10px"}}>Relación de diferencia de precios por promociones </h4>
        </div>

        <div>
        <p>&#9432; Ingresa el porcentaje de la diferencia entre la versión móvil y la versión web en caso de que la haya.  </p>

      </div>


        <br></br>
        <div>
          <p
            style={{
              display: "inline-block",
              margin: "10px",
              placeholder: "%",
            }}
          >
            Expedia
          </p>
          <input
        id="differenceRatioExp"
        type="number"
        placeholder="%"
        bsSize="sm"  // Tamaño pequeño
        style={{ margin: "10px" }}
          ></input>
          <p style={{ display: "inline-block", margin: "10px" }}>Booking</p>
          <input
        id="differenceRatioBbk"
        type="number"
        placeholder="%"
        bsSize="sm"  // Tamaño pequeño
        style={{ margin: "10px" }}
          ></input>
        </div>
      </form>
            <br></br>
      <Button
        type="submit"
        color="primary"
        style={{
          margin: "auto",
          border: 0,
          display: "inline-block",
          marginTop: "10px",
          marginBottom: "20px",
          marginRight: "40px",
        }}
      >
        Guardar y continuar
      </Button>

      <Button
        type="submit"
        onClick={toggle}
        style={{
          margin: "auto",
          border: 0,
          display: "inline-block",
          marginTop: "10px",
          marginBottom: "20px",
        }}
      >
        Ajustar valores
      </Button>
      <Modal isOpen={modal} toggle={toggle} {...args}>
        <ModalHeader toggle={toggle}>Actualizar URL´s</ModalHeader>
        <ModalBody>
          <FormGroup row>
            <Label for="urlHotel" sm={2}>
              Guruhotel:
            </Label>

            <Input
              id="urlHotel"
              name="url"
              placeholder="ej: https://www.maglenresort.com"
              type="text"
            />
          </FormGroup>

          <FormGroup row>
            <Label for="urlExpedia" sm={2}>
              Expedia:
            </Label>

            <Input
              id="urlExpedia"
              name="url_exp"
              placeholder="ej: https://www.expedia.com/maglen-resort..."
              type="text"
            />
          </FormGroup>
          <Label for="urlBooking" sm={2}>
            Booking:
          </Label>
          <Input
            id="urlBooking"
            name="url_bbk"
            placeholder="ej: https://www.booking.com/maglen-resort..."
            type="text"
          />
        </ModalBody>
        <ModalFooter>
          <Button color="primary" onClick={toggle}>
            Guardar y validar
          </Button>{" "}
          <Button color="secondary" onClick={toggle}>
            Cancelar
          </Button>
        </ModalFooter>
      </Modal>
    </div>
  );
}

export default AltaHotelRelacion;
