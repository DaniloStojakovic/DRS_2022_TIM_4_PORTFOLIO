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
         
    </div>
    
  )
}

export default NavBar