import React, { Component } from "react";
import { Button, Table } from "reactstrap";
import axios from "axios";
import { API_URL } from "../constants";


    const HotelDetail = () => {
        const handleClick = () => {
          axios.post('http://localhost:8000/api/hotel/h_full/')
            .then(response => {
              // Maneja la respuesta exitosa
              console.log('La función en Django se ejecutó correctamente');
            })
            .catch(error => {
              // Maneja los errores de la solicitud
              console.log('Hubo un error al ejecutar la función en Django:', error);
            });
        };
      
        return (
          <div>
            <button onClick={handleClick}>Ejecutar función en Django</button>
          </div>
        );
      };
      
      export default HotelDetail;
