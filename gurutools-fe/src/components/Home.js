import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import HotelList from "./HotelList";
import NewHotelModal from "./NewHotelModal";

import axios from "axios";
import { API_URL } from "../constants";


class Home extends Component {
    state = {
        Hotels: []
    };

    componentDidMount() {
        this.resetState();
    }

    getHotels = () => {
        axios.get(API_URL).then(res => this.setState({ Hotels: res.data }));
    };

    resetState = () => {
        this.getHotels();
    };

    render() {
        return (
            <Container style={{ marginTop: "20px" }}>
                <Row>
                    <Col>
                    <HotelList
                      Hotels={this.state.Hotels}
                      resetState={this.resetState}
                    />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <NewHotelModal create={true} resetState={this.resetState} />
                    </Col>
                </Row>
            </Container>
        );
    }
}

export default Home;