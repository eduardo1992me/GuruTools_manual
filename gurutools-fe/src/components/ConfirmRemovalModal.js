import React, { Component, Fragment } from "react";
import { Modal, ModalHeader, Button, ModalFooter } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class ConfirmRemovalModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  deleteHotel = pk => {
    axios.delete(API_URL + pk).then(()=> {
        this.props.resetState();
        this.toggle();
    });
  };

  render() {
    return (
        <Fragment>
        <Button color="danger" onClick={() => this.toggle()}>
          Borrar
        </Button>
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>
            ¿Estas seguro que quieres borrar el hotel?
          </ModalHeader>

          <ModalFooter>
            <Button type="button" onClick={() => this.toggle()}>
              Cancelar
            </Button>
            <Button
              type="button"
              color="primary"
              onClick={() => this.deleteHotel(this.props.pk)}
            >
              Si
            </Button>
          </ModalFooter>
        </Modal>
      </Fragment>
    );
  }
}

export default ConfirmRemovalModal;