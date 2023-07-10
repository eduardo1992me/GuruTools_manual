import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewHotelForm extends React.Component {
    state = {
        pk: 0,
        nombre: "",
        categoria: "",
        pais: "",
        estado: "",
        direccion: "",
        fecha_alta: "",
        activo: "1",
        id_usuario_id: ""
    };

    componentDidMount() {
        if (this.props.hotel) {
            const {pk, nombre, categoria, pais, estado, direccion, fecha_alta, activo, test, id_usuario_id} = this.props.hotel;
            this.setState({pk, nombre, categoria, pais, estado, direccion, fecha_alta, activo, test, id_usuario_id});
        }
    }

    onChange = e => {
        this.setState({[e.target.name]: e.target.value });
    };

    createHotel = e => {
        e.preventDefault();
        axios.post(API_URL, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };

    defaultIfEmpty = value => {
        return value === "" ? "" : value;
    };

    setStatus(event) {
        console.log(event.target.value);
      }

    render() {
        return (
            <Form onSubmit={this.props.hotel ? this.editHotel : this.createHotel}>
                <FormGroup>
                    <label for="nombre">Nombre:</label>
                    <Input
                        type="text"
                        name="nombre"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.nombre)}
                    />
                </FormGroup>
                <FormGroup>
                    <label for="categoria">Categoria:</label>
                    <Input
                        type="text"
                        name="categoria"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.categoria)}
                    />
                </FormGroup>
                <FormGroup>
                    <label for="pais">Pais:</label>
                    <Input
                        type="text"
                        name="pais"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.pais)}
                    />
                </FormGroup>
                <FormGroup>
                    <label for="estado">Estado:</label>
                    <Input
                        type="text"
                        name="estado"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.estado)}
                    />
                </FormGroup>
                <FormGroup>
                    <label for="direccion">Direccion:</label>
                    <Input
                        type="text"
                        name="direccion"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.direccion)}
                    />
                </FormGroup>
                <FormGroup>
                    <label for="fecha_alta">Fecha de alta:</label>
                    <Input
                        type="text"
                        name="fecha_alta"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.fecha_alta)}
                    />
                </FormGroup>

            <label for="activo">Habilitado:</label>

             <div onChange={this.setStatus}>
                <input type="radio" value="1" name="activo" defaultChecked/> Activo
                <br />
                <input type="radio" value="0" name="activo" /> Inactivo
                </div>
                <br />

                <FormGroup>
                <label for="activo">
                {this.state.activo === "1" ? "Activo" : "Inactivo"}
                </label>
                </FormGroup>
                
  
                <FormGroup>
                    <label for="id_usuario_id">Id de Usuario:</label>
                    <Input
                        type="text"
                        name="id_usuario_id"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.id_usuario_id)}
                    />
                </FormGroup>

                <Button>Guardar</Button>
            </Form>

        );
    }

}

export default NewHotelForm;