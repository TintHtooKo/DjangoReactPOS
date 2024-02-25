import React, { useEffect, useRef, useState } from 'react'
import './Product.css'
import axios from 'axios'
import { useReactToPrint } from 'react-to-print'
import { ComponentToPrint } from '../../components/ComponentToPrint'

export default function Product() {

  const[product,setProduct] = useState([])
  const[cart,setCart] = useState([])
  const [totalAmount,setTotalAmount] = useState(0);
  const [number,setNumber] = useState(1)



  const fatchProduct = async() =>{
    const result = await axios.get('http://localhost:8000/api/product/')
    setProduct(await result.data)
  }

  const addProductToCart = async(product)=>{
    // check if the adding product exist
    let findProductInCart = await cart.find(i=>{
        return i.id === product.id
    });

    if (findProductInCart){
        let newCart = [];
        let newItem;

        cart.forEach(cartItem =>{
            if(cartItem.id === product.id){
                newItem = {
                    ...cartItem,
                    quantity: cartItem.quantity + 1,
                    totalAmount: cartItem.price * (cartItem.quantity + 1)
                }
                newCart.push(newItem);
            }else{
                 newCart.push(cartItem);
            }
        });

        setCart(newCart);

    }else{
        let addingProduct = {
            ...product,
            'quantity':1,
            'totalAmount':product.price
        }
        setCart([...cart,addingProduct]);
    }
}

const removeProduct = async(product)=>{
    const newCart = cart.filter(cartItem => cartItem.id !== product.id);
    setCart(newCart);
}

const componentRef = useRef();

const handleReactToPrint = useReactToPrint({
    content: () => componentRef.current,
  });

const handlePrint = () =>{
    handleReactToPrint();
}

  useEffect(()=>{
    fatchProduct()
  },[])

  useEffect(()=>{
    let newTotalAmount = 0;
    cart.forEach(icart =>{
        newTotalAmount = newTotalAmount + parseInt(icart.totalAmount);            
    })
    setTotalAmount(newTotalAmount);
},[cart]);


  return (
    <div className='row'>
      <div className='view col-md-7'>
      {
        product.map((proD,index)=>{
          return(<div className='product' key={index} onClick={()=>addProductToCart(proD)}>
            <div className='image'><img src={`http://localhost:8000${proD.image}`}/></div>
            <div className='detail'>
                <h3>{proD.name}</h3>
                <p>$ {proD.price}</p>
            </div>
          </div>)
        })
      }
      </div>

      <div className='col-md-5'>
      <div style={{display:"none"}}>
                        <ComponentToPrint cart={cart} totalAmount={totalAmount} ref={componentRef}/>
                    </div>
        <h2 className='text-center mb-3'>Order List</h2>
        <table className="table">
            <thead>
                <tr>
                <th scope="col">No</th>
                <th scope="col">Product</th>
                <th scope="col">Qty</th>
                <th scope="col">Price</th>
                <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
            { cart.length > 0 ? cart.map((cartProduct, key)=>
                <tr key={key}>
                <th>{number + key}</th>
                <td>{cartProduct.name}</td>
                <td>{cartProduct.quantity}</td>
                <td>{cartProduct.totalAmount}</td>
                <td><button onClick={()=> removeProduct(cartProduct)}><i className='fa fa-trash' style={{cursor:"pointer",color:"red"}}/></button></td>
                </tr>
            ): 'No Item in cart'}
          </tbody>
          
        </table>
        <h3 className=' py-2'>Total Amount : ${totalAmount}</h3>
        <div className='mt-3'>
        {
            totalAmount !== 0 ? <div>
                <button className='btn btn-primary' onClick={handlePrint}>Pay Now</button>
            </div> : 'Please Add Product to cart'
        }
    </div>
    </div>

    

      
    </div>
  )
}
