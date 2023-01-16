import React from "react";
import '../Header.css';


const Header = () => {
    return (
    <div className="header">
        <a href="/">
          <img src="home.png" alt="Menu" className="menu-icon" />
        </a>
        <h1>Blockchain Bonanza</h1>
        <button className="sign-out-button">Sign Out</button>
    </div>
      
    );
  }
  
  export default Header;