import React, { Component } from 'react';
import './App.css';
import Home from './Home';
import Customers from './Customers';
import { Routes ,Route, BrowserRouter  } from 'react-router-dom';



class App extends Component {
  render() {
    return (
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="listCustomers" element={<Customers />} />        
      </Routes>
    </BrowserRouter>
    );
  }
}

export default App;
