import MonitoringDetailList from "./MonitoringDetailList";
import { Container, CardBody, Form, Card, Row, Table } from "reactstrap";
import MonitoringDetailInfo from './MonitoringDetailInfo'
import MDChartsBars from './MDChartsBars'
import { LineChart, Line } from 'recharts';
import MDChartsArea from "./MDChartsArea";
import MDCChartsPie from "./MDCChartsPie";
import MDCChartsLine from "./MDCChartsLine";
import MDCChartsMixBar from "./MDCChartsMixBar";

const data = [{name: 'Page A', uv: 400, pv: 2400, amt: 2400}];

function MonitoringDetail(args) {
  return (
    <div      style={{
        display: "block",

        padding: 30,
      }}>
        <MonitoringDetailInfo/>
       
        <div>
        <Row
        style={{
          margin: "1px",
          border: 0,
          display: "inline-block",
          marginTop: "10px",
          
          marginRight: "20px",
          width: "45%",
        }}
      >
        <h4 style={{textAlign: "center"}}>Precio Guruhotel Vs Otros Canales</h4>
        <br></br>

        <MDCChartsLine/>
        </Row>
        <Row
        style={{
          margin: "1px",
          border: 0,
          display: "inline-block",
          marginTop: "10px",
          width: "35%",
        }}
      >
        <h4 style={{textAlign: "center"}}>Disparidades por tipo de habitación(Últimos 30 días)</h4>
        <MDCChartsPie />

</Row>
<Row
        style={{
          margin: "1px",
          border: 0,
          display: "inline-block",
          marginTop: "10px",
          width: "17%",
        }}
      >
<p style={{color: "#2ecc71"}}> <strong>Doble, 2 Matrimoniales: 45</strong></p>
<p style={{color: "#74b9ff"}}> <strong>Sencilla, 1 individual: 25</strong></p>
<p style={{color: "#a29bfe"}}> <strong>Luxury, 1 king size: 7</strong></p>
<p style={{color: "#fab1a0"}}> <strong>Penthouse, 1 king California: 2</strong></p>

</Row>

        </div>
        <br></br>
        <br></br>
        <h4 style={{textAlign: "center"}}>Visitas del sitio web en los últimos 30 días(Google Analytics)</h4>
        <MDCChartsMixBar />
        <br></br>

      <Row >
        
        <h2>Lista de monitoreos: Maglen Resort</h2>
        
        <Card >
          <CardBody width="100%">
            <Form>
              <Table bordered hover responsive size="" striped>
                <thead>
                  <tr>
                    <th style={{ width: "10%" }}>Canal</th>
                    <th style={{ width: "22%" }}>Fecha de monitoreo</th>
                    <th style={{ width: "7%" }}>Moneda</th>
                    <th style={{ width: "12%" }}>Last Minute</th>
                    <th style={{ width: "12%" }}>7 días</th>
                    <th style={{ width: "12%" }}>30 días</th>
                    <th style={{ width: "12%" }}>90 días</th>
                    <th>Acciones</th>
                  </tr>
                </thead>
              </Table>
              

              <MonitoringDetailList />
              <MonitoringDetailList />
              <MonitoringDetailList />
            </Form>
          </CardBody>
        </Card>
      </Row>
    </div>
  );
}

export default MonitoringDetail;
