import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      // Sending login request to your Node.js backend
      const res = await axios.post('http://localhost:5000/api/auth/login', {
        email,
        password,
      });

      // Saving the security token in your browser
      localStorage.setItem('token', res.data.token);
      localStorage.setItem('user', JSON.stringify(res.data.user));

      alert("Login Successful! Welcome back.");
      navigate('/'); // Redirect to Home page
    } catch (err) {
      alert("Error: " + (err.response?.data?.message || "Invalid Email or Password"));
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '50px' }}>
      <div style={{ width: '350px', padding: '20px', border: '1px solid #ddd', borderRadius: '5px', backgroundColor: 'white' }}>
        <h2 style={{ marginBottom: '20px', fontWeight: '500' }}>Sign-In</h2>
        
        <form onSubmit={handleLogin}>
          <h5 style={{ marginBottom: '5px' }}>E-mail</h5>
          <input 
            type="email" 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
            required 
            style={{ width: '100%', marginBottom: '15px', padding: '8px' }} 
          />

          <h5 style={{ marginBottom: '5px' }}>Password</h5>
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            required 
            style={{ width: '100%', marginBottom: '20px', padding: '8px' }} 
          />

          <button 
            type="submit" 
            style={{ width: '100%', backgroundColor: '#f0c14b', border: '1px solid #a88734', padding: '8px', cursor: 'pointer', borderRadius: '3px' }}>
            Sign In
          </button>
        </form>

        <p style={{ marginTop: '15px', fontSize: '12px' }}>
          By signing-in you agree to the Amazon Clone Conditions of Use & Sale.
        </p>

        <Link to="/register">
          <button style={{ width: '100%', marginTop: '15px', padding: '8px', cursor: 'pointer', border: '1px solid darkgray', borderRadius: '3px' }}>
            Create your Amazon Account
          </button>
        </Link>
      </div>
    </div>
  );
}

export default Login;