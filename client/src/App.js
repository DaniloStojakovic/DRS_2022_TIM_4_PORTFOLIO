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
