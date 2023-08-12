import { React } from "react";
import { Row, Card, CardBody, Form, Table, Button } from "reactstrap";

function MonitoringDetailInfo() {
  return (
    <div>
      <Row
        style={{
          margin: "auto",
          border: 0,
          display: "inline-block",
          marginTop: "10px",
          marginBottom: "20px",
          width: "78%",
        }}
      >
        <h1>Maglen Resort</h1>

        <Card>
          <CardBody width="100%">
            <Form>
              <h4>Información General</h4>
              <Table>
                <thead>
                  <tr>
                    <th>Account Manager: Andres Suarez</th>
                    <th>Categoría: Business Class</th>
                  </tr>
                  <tr>
                    <th>URL: https://www.maglenresort.com/</th>
                    <th>País: México</th>
                  </tr>
                  <tr>
                    <th>Estado/Provincia: Baja California</th>
                    <th>
                      Dirección: México 3 Km. 90.8, Fraccionamiento Las Lomas,
                      22766 Villa de Juárez, B.C.
                    </th>
                  </tr>
                </thead>
              </Table>
              <div className="d-flex justify-content-end">
                <Button type="submit" color="secondary" className="ml-auto">
                  Editar
                </Button>
              </div>
            </Form>
          </CardBody>
        </Card>
      </Row>

      <Row
        style={{
          margin: "10px",
          border: 0,
          display: "inline-block",
          marginTop: "10px",
          width: "19%",
        }}
      >
        <Card>
          <CardBody width="100%">
            <Form>
              <h4>Canales enlazados</h4>
              <Table>
                <thead>
                  <tr>
                    <th>Sitio Web:</th>
                    <th>Activo</th>
                  </tr>
                  <tr>
                    <th>Expedia:</th>
                    <th>Activo </th>
                  </tr>
                  <tr>
                    <th>Booking:</th>
                    <th>Activo</th>
                  </tr>
                </thead>
              </Table>
              <div className="d-flex justify-content-end">
                <Button type="submit" color="secondary" className="ml-auto">
                  Editar
                </Button>
              </div>
            </Form>
          </CardBody>
        </Card>
      </Row>
    </div>
  );
}

export default MonitoringDetailInfo;
