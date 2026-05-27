const mongoose = require('mongoose');

const productSchema = mongoose.Schema({
    title: String,
    price: Number,
    image: String,
    rating: Number,
});

module.exports = mongoose.model('Product', productSchema);