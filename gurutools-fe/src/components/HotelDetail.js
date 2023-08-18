import React, { Component, Fragment } from "react";
import { Button, Table } from "reactstrap";
import axios from "axios";
import { API_URL } from "../constants";




function HotelDetail() {
  const handleClick = () => {
    axios.post('http://localhost:8000/api/hotel/h_full/')
      .then(response => {
        // Maneja la respuesta exitosa
      })
      .catch(error => {
        // Maneja los errores de la solicitud
        console.log(error);
      });
  };

  
    return (
        
      <Fragment>
      <div>
        <button onClick={handleClick}>Ejecutar función en Django</button>
      </div>
      </Fragment>
    );
  };


export default HotelDetail