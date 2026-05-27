import React from 'react';

function Cart({ items, removeFromCart }) {
  // To calculate the total price of all items in the cart
  const totalPrice = items.reduce((total, item) => total + item.price, 0);

  return (
    <div style={{ padding: '20px', backgroundColor: 'white', margin: '20px', borderRadius: '8px', border: '1px solid #ddd', boxShadow: '0 2px 10px rgba(0,0,0,0.1)' }}>
      <h2 style={{ borderBottom: '2px solid #eee', paddingBottom: '10px' }}>Your Shopping Cart</h2>
      
      {items.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '30px' }}>
          <h3>Your Amazon Cart is empty.</h3>
          <p>Add some products to see them here!</p>
        </div>
      ) : (
        <div>
          {/* Using map() to display every item in the cart */}
          {items.map((item, index) => (
            <div key={index} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '15px 0', borderBottom: '1px solid #eee' }}>
              <div>
                <h4 style={{ margin: '0 0 5px 0' }}>{item.title}</h4>
                <p style={{ margin: 0, color: '#B12704', fontWeight: 'bold' }}>₹{item.price.toLocaleString('en-IN')}</p>
              </div>
              
              {/* Remove Button Logic */}
              <button 
                onClick={() => removeFromCart(index)}
                style={{ 
                  backgroundColor: '#f0f2f2', 
                  border: '1px solid #d5d9d9', 
                  padding: '5px 15px', 
                  borderRadius: '8px', 
                  cursor: 'pointer', 
                  color: '#CC0C39',
                  fontWeight: 'bold',
                  fontSize: '12px'
                }}>
                Remove
              </button>
            </div>
          ))}
          
          {/* Total Price Section */}
          <div style={{ textAlign: 'right', marginTop: '20px', padding: '10px', backgroundColor: '#f9f9f9', borderRadius: '5px' }}>
            <h3 style={{ margin: '0' }}>Subtotal ({items.length} items): 
              <span style={{ color: '#B12704', marginLeft: '10px' }}>₹{totalPrice.toLocaleString('en-IN')}</span>
            </h3>
            <button style={{ 
              backgroundColor: '#ffd814', 
              border: '1px solid #fcd200', 
              padding: '10px 30px', 
              borderRadius: '20px', 
              fontWeight: 'bold', 
              cursor: 'pointer',
              marginTop: '15px',
              width: '200px'
            }}>
              Proceed to Buy
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Cart;