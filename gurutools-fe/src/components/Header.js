import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
        <div className="text-center">
          <img
            src="https://www.guruhotel.com/hubfs/guruhotel-logo-1.svg"
            width="300"
            className="img-thumbnail"
          />
          <hr />
          <h1>Guru Tools</h1>
          <br></br>
        </div>
      );
    }
  }
  
  export default Header;