import React, { Component } from "react";
import { Table } from "reactstrap";
import NewHotelModal from "./NewHotelModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class HotelList extends Component {
    render () {
        const Hotels = this.props.Hotels;
        return (
            <Table dark>
              <thead>
          <tr>
            <th>Nombre</th>
            <th>Categoria</th>
            <th>País</th>
            <th>Estado</th>
            <th>Dirección</th>
            <th>Fecha de alta</th>
            <th>Activo</th>
            <th>Acciones</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!Hotels || Hotels.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, Aún ninguno</b>
              </td>
            </tr>
          ) : (
            Hotels.map(hotel => (
              
              <tr key={hotel.pk}>
                
                <td>{hotel.nombre}</td>
                <td>{hotel.categoria}</td>
                <td>{hotel.pais}</td>
                <td>{hotel.estado}</td>
                <td>{hotel.direccion}</td>
                <td>{hotel.fecha_alta}</td>
                <td>{hotel.activo.toString()}</td>
                
                <td align="center">
                  
                <NewHotelModal
                    create={false}
                    hotel={hotel}
                    resetState={this.props.resetState}
                  />


                  <ConfirmRemovalModal
                    pk={hotel.pk}
                    resetState={this.props.resetState}
                  />
                  
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default HotelList;