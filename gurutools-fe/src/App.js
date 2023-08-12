import "./App.css";
import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import Home from "./components/Home";
import LoginForm from "./components/Login";
import MonitoringButton from "./components/HotelDetail";
import AltaHotel from "./components/AltaHotel";
import AltaHotelRelacion from "./components/AltaHotelRelacion";
import CalendarT from "./components/CalendarT";
import MonitoringDetail from "./components/MonitoringDetailGroup/MonitoringDetail";

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <Home />
        <AltaHotel/>
        <AltaHotelRelacion/>

        <MonitoringDetail />
       
      </Fragment>
    );
  }
}

//function App() {
//  return (
//    <div className="App">
//      <header className="App-header">
//        <img src={logo} className="App-logo" alt="logo" />
//        <p>
//          Edit <code>src/App.js</code> and save to reload.
//        </p>
//        <a
//          className="App-link"
//          href="https://reactjs.org"
//          target="_blank"
//          rel="noopener noreferrer"
//        >
//          Learn React
//        </a>
//      </header>
//    </div>
//  );
//}
//
export default App;
