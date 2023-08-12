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
} from "reactstrap";

function MonitoringDetailList(args) {
  const [modal, setModal] = useState(false);
  const toggle = () => setModal(!modal);
  return (
    <div
    style={{
        display: "block",
      }}
    >
      <Table  bordered hover responsive size="" striped>

        <tbody>
          <tr>
            
            <td style={{width: "10%"}}>Sitio Web</td>
            <td style={{width: "22%"}}>25/agosto/2023, 10:02 am</td>
            <td style={{width: "7%"}}>USD</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
          </tr>

          <tr>
           
        
            <td style={{width: "10%"}}>Expedia</td>
            <td style={{width: "22%"}}>25/agosto/2023, 10:02 am</td>
            <td style={{width: "7%"}}>USD</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
            <td>
              <Button
                type="submit"
                onClick={toggle}
                style={{ margin: "auto", border: 0, display: "inline-block" }}
              >
                Ver detalle
              </Button>
            </td>
          </tr>
          <tr>
            <td style={{width: "10%"}}>Booking</td>
            <td style={{width: "17%"}}>25/agosto/2023, 10:03 am</td>
            <td style={{width: "7%"}}>USD</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
            <td style={{ background: "#ff7675", width: "12%" }}>Con incidencias</td>
            <td style={{width: "12%"}}>Sin incidencias</td>
          </tr>
        </tbody>
      </Table>

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
      </Modal>
    </div>
  );
}
export default MonitoringDetailList;
