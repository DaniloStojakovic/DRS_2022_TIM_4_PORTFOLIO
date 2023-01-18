import React from 'react';
import {useState, useEffect} from 'react';
import '../Register.css';
import axios from 'axios'
import ReactDOM from 'react-dom/client';



function Register() {
  const [usernameReg, setUsernameReg] = useState("");
  const register1 = (event) => {
    event.preventDefault();
    let data = ({
      inputUsername: document.getElementById('inputUsername').value,
      inputSurname: document.getElementById('inputSurname').value,
      inputAddress: document.getElementById('inputAddress').value,
      inputState: document.getElementById('inputState').value,
      inputNumber: document.getElementById('inputNumber').value,
      inputEmail: document.getElementById('inputEmail').value,
      inputPassword: document.getElementById('inputPassword').value
    })
    console.log(data );
    axios.post('http://localhost:5050/register', data,
    {
    headers:{
      'Accept': 'application/json, text/plain, /',
      'Content-Type': 'application/json'
    }})
    .then(response => 
        // Handle successful response
        alert(response),setUsernameReg("nela")
    )
    .catch(error => {
        // Handle error
    });
  
  }
  if(usernameReg=="nela"){
    const root1 = ReactDOM.createRoot(document.getElementById('root'));
  root1.render(<Register/>
  );
  }
  
    return (
        <div><h1>Registration</h1>
            <form>
            <label>Username:</label>
            <input 
                id='inputUsername'
                name='inputUsername'
                type="text" 
                onChange={(e) => {
                setUsernameReg(e.target.value);
                }}/>
            <br></br>
            <label>Surname: </label>
            <input id='inputSurname' name='inputSurname' type="text" />
            <br></br>
            <label>Address: </label>
            <input id='inputAddress' name='inputAddresss' type="text" />
            <br></br>
            <label>State: </label>
            <input id='inputState' name='inputState' type="text" />
            <br></br>
            <label>Telephone number: </label>
            <input id='inputNumber' name='inputNumber' type="text" />
            <br></br>
            <label>Email: </label>
            <input id='inputEmail' name='inputEmail' type="text" />
            <br></br>
            <label>Password: </label>
            <input 
                id='inputPassword'
                name='inputPassword'
                type="text"/>
            <br></br>
            <button type='submit' onClick={register1}>Register</button>
            <br/>
            </form>
            </div>
    )
  }
export default Register
