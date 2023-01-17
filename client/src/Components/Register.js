import React from 'react';
import {useState, useEffect} from 'react';
import '../Register.css';
import axios from 'axios'




function Register(){

    const [usernameReg, setUsernameReg] = useState("");
    const [passwordReg, setPasswrodReg] = useState("");

    const register=e=>{
            
        e.preventDefault();
            return axios.post(`http://localhost:5000/register`) 
                .then(res=>alert(res)) 
        
    }


    return(
        <div>            <h1>Registration</h1>
            <label>Username:</label>
            <form onSubmit={register}>
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
            <input type={"submit"} name='registruj' value={"Register"}></input>
            <br/>
            </form>
            </div>

    )
}

export default Register
