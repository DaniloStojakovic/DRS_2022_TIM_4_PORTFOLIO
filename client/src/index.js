import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import UserPortfolio from './Pages/UserPortfolio';
import UserModify from './Pages/UserModify';
import CryptoStore from './Pages/CryptoStore';
import {
  createBrowserRouter,
  RouterProvider,
  Route,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
  },
  {
    path: "UserPortfolio",
    element: <UserPortfolio/>,
  },
  {
    path: "UserModify",
    element: <UserModify/>,
  },
  {
    path: "CryptoStore",
    element: <CryptoStore/>,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router ={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
