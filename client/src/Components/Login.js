import React from 'react';
import '../Login.css';
import axios from 'axios';
import Header from './Header';


const login1 = () => {
  let data = JSON.stringify({
    name: document.getElementById('name').value,
    input_passsword: document.getElementById('input_passsword').value
  })
  console.log(data );
  axios.post('http://localhost:5000/login', data,
  {
  headers:{
    'Accept': 'application/json, text/plain, */*',
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
            <input id='name' name='name' type ="name" placeholder="Username" />
            <br></br>
            <input id='input_passsword' name='input_passsword' type="text" placeholder="Password" />
            <br></br>
            <button type='submit' onClick={this.login1}>Login</button>  
          </div>
        </form>
    )
  }
  
export default Login
