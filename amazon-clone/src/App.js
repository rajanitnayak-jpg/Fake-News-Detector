import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import axios from 'axios';
import ProductDetails from './ProductDetails'; 
import Cart from './Cart';
import Login from './Login'; // Make sure you created Login.js

function App() {
  const [cartItems, setCartItems] = useState([]);
  const [products, setProducts] = useState([]);

  // 1. Fetch Products from Backend
  useEffect(() => {
    axios.get('http://localhost:5000/api/products')
      .then(res => setProducts(res.data))
      .catch(err => console.error("Database connection error:", err));
  }, []);

  // 2. Cart Functions
  const addToCart = (product) => {
    setCartItems([...cartItems, product]);
  };

  const removeFromCart = (indexToRemove) => {
    const updatedCart = cartItems.filter((_, index) => index !== indexToRemove);
    setCartItems(updatedCart);
  };

  return (
    <Router>
      <div style={{ backgroundColor: '#EAEDED', minHeight: '100vh' }}>
        
        <Routes>
          {/* LOGIN PAGE */}
          <Route path="/login" element={<Login />} />

          {/* HOME PAGE (Store) */}
          <Route path="/" element={
            <>
              <header style={{ backgroundColor: '#131921', color: 'white', padding: '15px', textAlign: 'center' }}>
                <h1>Amazon Clone</h1>
                <p style={{ fontWeight: 'bold', color: '#febd69' }}>Items in Cart: {cartItems.length}</p>
                <a href="/login" style={{ color: 'white', textDecoration: 'none', fontSize: '14px' }}>Sign In</a>
              </header>

              <div style={{ padding: '20px' }}>
                <ProductDetails products={products} addToCart={addToCart} />
              </div>

              <hr style={{ margin: '40px 0', border: '1px solid #ddd' }} />
              
              <Cart items={cartItems} removeFromCart={removeFromCart} />
            </>
          } />
        </Routes>

        <footer style={{ textAlign: 'center', padding: '20px', color: '#555' }}>
          <p>© 2024 Amazon Clone Project - Full Stack Completed</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;