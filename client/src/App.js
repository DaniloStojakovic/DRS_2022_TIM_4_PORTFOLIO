import './App.css';
import {useState, useEffect} from 'react';
import { Channel } from './Components/Channel/Channel'
import Login from './Components/Login';
import Register from './Components/Register';
import Header from './Components/Header';


function App() {

  const [initialState, setState] = useState([])
  const url = '/api'
/*
  fetch('/registser', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name: "John", email: "john@example.com" })
  })
  .then(response => response.text())
  .then(data => console.log(data))
  .catch(error => console.error(error))

*/

useEffect(()=>{
  fetch(url,{
    'methods':'GET',
    headers : {
      'Content-Type':'application/json'
    }
  })
  .then(response => response.json())
  .catch(error => console.log(error))

},[])
/*
  return (
    <div className="App">
      <Channel data={initialState}/>
    </div> 
  )

*/ 
    return(
      <div className='App'>
        <Header></Header>
        <Login />
        <Register />
      </div>
    )

}

export default App;
