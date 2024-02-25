import React, { useState } from "react";



export const ComponentToPrint = React.forwardRef((props, ref) => {
    const {cart,totalAmount} = props;
    const [no,setNo] = useState(1)
    return (
      <div ref={ref} className="p-5">
        <table className='table'>
                            <th>
                                <thead>
                                    <tr>
                                        <td>#</td>
                                        <td>Name</td>
                                        <td>Price</td>
                                        <td>Qty</td>
                                        <td>Total</td>
                                    </tr>
                                </thead>
                                <tbody>
                                    { cart.length > 0 ? cart.map((cartProduct, key)=>
                                    <tr key={key}>
                                        <td>{no + key}</td>
                                        <td>{cartProduct.name}</td>
                                        <td>{cartProduct.price}</td>
                                        <td>{cartProduct.quantity}</td>
                                        <td>{cartProduct.totalAmount}</td>
                                        
                                    </tr>
                                    ):''}
                                </tbody>
                            </th>
                        </table>
                        <h2 className='px-2'>Total Amount : ${totalAmount}</h2>
      </div>
    );
  });