import React from 'react';
import {useState, useEffect} from 'react';
import '../Register.css';




function Register(){

    const [usernameReg, setUsernameReg] = useState("");
    const [passwordReg, setPasswrodReg] = useState("");

    return(
        <div className="register">
            <h1>Registration</h1>
            <label>Username:</label>
            <input 
                type="text" 
                onChange={(e) => {
                setUsernameReg(e.target.value);
                }}/>
            <br></br>
            <label>Surname: </label>
            <input type="text" />
            <br></br>
            <label>Address: </label>
            <input type="text" />
            <br></br>
            <label>State: </label>
            <input type="text" />
            <br></br>
            <label>Telephone number: </label>
            <input type="text" />
            <br></br>
            <label>Email: </label>
            <input type="text" />
            <br></br>
            <label>Password: </label>
            <input 
                type="text" 
                onChange={(e) => {
                setPasswrodReg(e.target.value);
                }}/>
            <br></br>
            <button>Register</button>
        </div>
    )
}

export default Register
