import './App.css';
import {useState, useEffect} from 'react';
import { Channel } from './Components/Channel/Channel'

function App() {

  const [initialState, setState] = useState([])
  const url = '/api'

  useEffect(()=>{
    fetch(url).then(response => {
      if(response.status === 200){
        return response.json()
      }
    }).then(data => setState(data))
  }, [])
/*
  return (
    <div className="App">
      <Channel data={initialState}/>
    </div> 
  )

*/ 
  const [usernameReg, setUsernameReg] = useState("");
  const [passwordReg, setPasswrodReg] = useState("");

  return(
    <div className="App">
      <div className="registration">
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
      <div className="login">
        <h1>Login</h1>
        <input type="text" placeholder="Username" />
        <br></br>
        <input type="text" placeholder="Password" />
        <br></br>
        <button>Login</button>
      </div>
      
    </div>
  )
  

  }

export default App;
