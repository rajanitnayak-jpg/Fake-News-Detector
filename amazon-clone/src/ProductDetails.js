import React from 'react';

// Notice we are now taking "products" as a prop from App.js
function ProductDetails({ products, addToCart }) {
  
  // If the backend is still loading or empty, show a message
  if (!products || products.length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '50px' }}>
        <h2>Loading products from Backend...</h2>
        <p>Make sure your Node.js server is running and MongoDB has data.</p>
      </div>
    );
  }

  return (
    <div style={{ padding: '20px' }}>
      <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>Amazon Deals - Shop Our Best Sellers</h2>
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))', 
        gap: '20px',
        maxWidth: '1200px',
        margin: '0 auto'
      }}>
        {products.map((product) => (
          <div key={product._id} style={{ 
            backgroundColor: 'white', padding: '20px', borderRadius: '4px',
            display: 'flex', flexDirection: 'column', justifyContent: 'space-between',
            boxShadow: '0 1px 3px rgba(0,0,0,0.1)'
          }}>
            <div style={{ textAlign: 'center' }}>
              {/* Product Image */}
              <img 
                src={product.image} 
                alt={product.title} 
                style={{ height: '150px', maxWidth: '100%', objectFit: 'contain', marginBottom: '10px' }} 
              />
              <h3 style={{ fontSize: '16px', fontWeight: '500', height: '40px', overflow: 'hidden' }}>
                {product.title}
              </h3>
            </div>
            <div>
              {/* Product Price */}
              <p style={{ fontSize: '18px', fontWeight: 'bold', margin: '10px 0' }}>
                ₹{product.price ? product.price.toLocaleString('en-IN') : '0'}
              </p>
              
              {/* Add to Cart Button */}
              <button 
                onClick={() => addToCart(product)}
                style={{ 
                  width: '100%', padding: '8px', backgroundColor: '#ffd814', 
                  border: '1px solid #fcd200', borderRadius: '20px', cursor: 'pointer', fontWeight: '500'
                }}>
                Add to Cart
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductDetails;