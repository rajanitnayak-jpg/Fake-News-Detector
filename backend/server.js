const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

const app = express();

// 1. Middleware
app.use(cors());
app.use(express.json()); // Allows the server to read JSON data from the frontend

// 2. Database Connection
mongoose.connect(process.env.MONGO_URI)
    .then(() => console.log("✅ MongoDB Connected Successfully"))
    .catch(err => console.log("❌ MongoDB Connection Error:", err));

// 3. API Routes
// Product Routes
app.use('/api/products', require('./routes/productRoutes'));

// Auth Routes (Login & Register)
app.use('/api/auth', require('./routes/authRoutes'));

// 4. Basic Health Check
app.get('/', (req, res) => {
    res.send("Amazon Clone Backend API is Live!");
});

// 5. Server Port Setup
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`🚀 Server is running on port ${PORT}`);
});