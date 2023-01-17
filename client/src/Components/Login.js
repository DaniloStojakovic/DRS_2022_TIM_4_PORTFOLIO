import React from 'react';
import '../Login.css';
import axios from 'axios';
import Header from './Header';


const login1 = () => {
  let data = ({
    inputUsername: document.getElementById('inputUsername').value,
    inputPassword: document.getElementById('inputPassword').value
  })
  console.log(data );
  axios.post('http://localhost:5000/api/login', data,
  {
  headers:{
    'Accept': 'application/json, text/plain, /',
    'Content-Type': 'application/json'
  }})
  .then(response => {
      // Handle successful response
  })
  .catch(error => {
      // Handle error
  });
}

function Login() {
    return (
        <form action='/login' method='POST'>
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