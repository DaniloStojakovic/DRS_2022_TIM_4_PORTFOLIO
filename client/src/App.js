import './App.css';
import {useState, useEffect} from 'react';
import { Channel } from './Components/Channel/Channel'
import Login from './Components/Login';
import Register from './Components/Register';
import Header from './Components/Header';
import axios from 'axios';

function App() {

  const [initialState, setState] = useState([])
  const url = '/api'


axios.get('http://localhost:80/')
  .then(response => console.log(response.data))
  .catch(error => console.log(error))



/*
  useEffect(()=>{
    fetch(url).then(response => {
      if(response.status === 200){
        return response.json()
      }
    }).then(data => setState(data))
  }, [])
*/
  
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
