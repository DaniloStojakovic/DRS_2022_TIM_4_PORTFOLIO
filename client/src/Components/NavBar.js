import React from 'react'
import { Link } from "react-router-dom";
import '../NavBar.css';
import { useState } from "react";

function NavBar() {

    const [isNavExpanded, setIsNavExpanded] = useState(false)


    return (
    <div className="navbar">
        <p className="brand-name">
            Blockchain Bonanza
        </p>
        <div className="navigation-menu">
            <ul>
                <li>
                    <Link to ="/">
                        Home         {/* ->UserPortfolio */}
                    </Link>
                </li>
                <li>
                    <Link to ="/CryptoStore">
                        Crypto Store {/* ->CryptoStore */}
                    </Link>
                </li>
                <li>
                    <Link>
                        Transactions {/* 6. Brisanje neke kriptovalute ili neke kupovine/prodaje */}
                    </Link>
                </li>
                <li>
                    <Link to="/UserModify">
                        Profile     {/* ->UserModify */}
                    </Link>
                </li>
            </ul>
        </div>
        <button className="menu" onClick={() => {
          setIsNavExpanded(!isNavExpanded);
        }}>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 5.25h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5" />
        </svg>
        </button>
        <div className={
          isNavExpanded ? "navigation-menu expanded" : "navigation-menu"
        }>
            <ul>
                <li>
                    <Link to ="/">
                        Home         {/* ->UserPortfolio */}
                    </Link>
                </li>
                <li>
                    <Link to ="/CryptoStore">
                        Crypto Store {/* ->CryptoStore */}
                    </Link>
                </li>
                <li>
                    <Link>
                        Transactions {/* 6. Brisanje neke kriptovalute ili neke kupovine/prodaje */}
                    </Link>
                </li>
                <li>
                    <Link to="/UserModify">
                        Profile     {/* ->UserModify */}
                    </Link>
                </li>
            </ul>
      </div>  
    </div>
    
  )
}

export default NavBar