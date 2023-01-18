import React from 'react';
import '../Login.css';
import axios from 'axios';
import Header from './Header';
import ReactDOM from 'react-dom/client';
import {useState, useEffect} from 'react';
import App from '../App';
import Register from './Register';
import UserPortfolio from '../Pages/UserPortfolio';
import NavBar from './NavBar';




function Login() {
  const [usernameReg, setUsernameReg] = useState("");
  const login1 = (event) => {
    event.preventDefault();
    let data = ({
      inputUsername: document.getElementById('inputUsername').value,
      inputPassword: document.getElementById('inputPassword').value
    })
    console.log(data );
    axios.post('http://localhost:5050/login', data,
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
  root1.render(<Login/>
  );
  }
  
    return (
        <form>
          <div className="login">
            <h1>Login</h1>
            <input id='inputUsername' name='inputUsername' type ="name" placeholder="Username" />
            <br></br>
            <input id='inputPassword' name='inputPassword' type="text" placeholder="Password" />
            <br></br>
            <button type='submit' onClick={login1}>Login</button>
          </div>
        </form>
    )
  }

export default Login