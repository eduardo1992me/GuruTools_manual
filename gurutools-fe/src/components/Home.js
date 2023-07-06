import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import HotelList from "./HotelList";
import NewHotelModal from "./NewHotelModal";

import axios from "axios";
import { API_URL } from "../constants";


class Home extends Component {
    state = {
        hotels: []
    };

    componentDidMount() {
        this.resetState();
    }

    getHotels = () => {
        axios.get(API_URL).then(res => this.setState({ hotels: res.data }));
    };

    resetState = () => {
        this.getHotels();
    };

    render() {
        return (
            <Container>
                <Row>
                    <Col>
                    <HotelList
                      hotels={this.state.hotels}
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