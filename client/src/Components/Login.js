import React from 'react';
import '../Login.css';


function Login() {
    return (  
        <div className="login">
          <h1>Login</h1>
          <input type ="text" placeholder="Username" />
          <br></br>
          <input type="text" placeholder="Password" />
          <br></br>
          <button>Login</button>  
      </div>
    )
  }
  
export default Login
