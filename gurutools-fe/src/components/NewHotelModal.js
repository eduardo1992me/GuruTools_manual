import React, {Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewHotelForm from "./NewHotelForm";

class NewHotelModal extends Component {
    state = {
        modal: false
    };

    toggle = () => {
        this.setState(previous => ({
            modal: !previous.modal
        }));
    };

    render() {
        const create = this.props.create;

        var title = "Editando Hotel";
        var button = <Button onClick={this.toggle}>Editar</Button>;
        
        if (create) {
            title = "Creando nuevo Hotel";

            button = (
                <Button
                    color="primary"
                    className="float-right"
                    onClick={this.toggle}
                    style={{ minWidth: "200px"}}
                    
                >
                    Crear nuevo hotel 
                </Button>

            );
        }
        return (
            <Fragment>
                {button}
                <Modal isOpen={this.state.modal} toggle={this.toggle}>
                    <ModalHeader toggle={this.toggle}>{title}</ModalHeader>
                    <ModalBody>
                        <NewHotelForm
                        resetState={this.props.resetState}
                        toggle={this.toggle}
                        hotel={this.props.hotel}
                        />
                    </ModalBody>
                </Modal>
            </Fragment>
        )
    }
}

export default NewHotelModal;