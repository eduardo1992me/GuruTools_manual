import { useState } from "react";
import { Input, Button } from "reactstrap";
import Son from './Info_transfer_des'; /* <---- */

function Info_transfer_origin() {
  const [state, setState] = useState({
    num1: 0,
    num2: 0,
    result: 0, /* <---- */
  });

  const onChange = (e) => {
    setState({...state, [e.target.name]: e.target.value });
    console.log(state)
  };
  
  const defaultIfEmpty = (value) => (value === "" ? "" : value);

  const multiplicacion = () => {
        let result = state.num1 * state.num2
        console.log(result)
        setState({ ...state, result: result }); /* <---- */
        setShowSonComponent(true);
        
    };

  const [showSonComponent, setShowSonComponent] = useState(false);


  return (
    <div>
      <h1>En este componente se tiene un numero</h1>
      <Input type="number" name="num1" onChange={onChange} value={defaultIfEmpty(state.num1)}  style={{ margin: "10px" }}>
        Ingresa un mumero
      </Input>
      <Input type="number" name="num2" onChange={onChange} value={defaultIfEmpty(state.num2)} style={{ margin: "10px" }}>
        Ingresa el segundo numero
      </Input>
      
      <Button onClick={multiplicacion}>Multiplicar</Button>
      {showSonComponent && <Son data={state.result} />} {/* <---- */}
    </div>
  );
}

export default Info_transfer_origin;
