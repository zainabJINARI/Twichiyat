const categories = document.getElementById('categoriesnav')

function AddI(e,quantite){
    
    const inputElt = e.target.offsetParent.querySelector('input[type="text"]')
    let currentValue = parseInt(inputElt.value, 10) || 0;
    quantite=parseInt(quantite, 10)
  
    if (quantite > currentValue){
        console.log(inputElt)
        inputElt.value = currentValue + 1; 
    }
}
function SubI(e){
    const inputElt = e.target.offsetParent.querySelector('input[type="text"]')
    let currentValue = parseInt(inputElt.value, 10) || 0;
    if (currentValue>1){
        inputElt.value = currentValue - 1; 
    }
}

function displayCartList(){
    let cartListDis=JSON.parse(localStorage.getItem('cartList'))
    cartContainer.style.display='flex'
    console.log(cartListDis)
    if(!cartListDis || cartListDis.length == 0){
        document.getElementById('cart-items').style.display='none'
        document.querySelector('div[class="no-items"]').style.display='flex'
       
    }else{
        document.getElementById('cart-items').innerHTML=""
        console.log('items exit')
        cartListDis.forEach(element => {
            // quantite=element.quan
            const containeritem = document.createElement('div')
            containeritem.classList.add('cart-item')
            containeritem.setAttribute('id', 'cart-item')
            const closebnt = document.createElement('span')
            closebnt.innerHTML='&times;'
            closebnt.classList.add('remove-item')
            
            
            const div = document.createElement('div')
            div.innerHTML+=`
                <img src=${element.img} alt="" width="70px">
            `
            
            const divInfo = document.createElement('div')
            divInfo.classList.add('info')
            divInfo.innerHTML+=`
                                <div class="base-info">
                                    <h5>${element.name}</h5>
                                    <p>${element.size}</p>
                                    <p>${element.price}</p>
                                </div>
            `
            
            const divCarQuant = document.createElement('div')
            divCarQuant.classList.add('cart-quant')


        
            const btnAdd = document.createElement('button')
            btnAdd.innerHTML+=`
                <i class="fa-solid fa-plus" style="color: #302219;"></i>
            `
            
            const btnSub = document.createElement('button')
            btnSub.innerHTML+=`
                <i class="fa-solid fa-minus" style="color: #302219;"></i>
            `
          
            // btnSub.setAttribute('onclick', 'SubI()') 
            input = document.createElement('input')
            input.setAttribute('type',"text")
            // input.setAttribute('id','valueQ')
            input.setAttribute('value',element.quan)
            btnAdd.addEventListener('click', (e) => AddI(e,element.maxquant));
            btnSub.addEventListener('click', (e) => SubI(e));
            
            divCarQuant.appendChild(btnAdd)
            divCarQuant.appendChild(input)
            divCarQuant.appendChild(btnSub)
            divInfo.appendChild(divCarQuant)
            closebnt.addEventListener('click', (e) => {
                
                cartListDis = cartListDis.filter(item => {
                    
                    console.log(item)
                    console.log(element.idProd)
                    console.log(item.idProd != element.idProd)
                    return item.idProd != element.idProd
                    
                })  
                console.log(cartListDis)
                localStorage.setItem('cartList', JSON.stringify(cartListDis))
                
                displayCartList()
            })
            containeritem.appendChild(closebnt)
            containeritem.appendChild(div)
            containeritem.appendChild(divInfo)
            
            document.getElementById('cart-items').appendChild(containeritem)
            
            
        });
        


        document.getElementById('cart-items').style.display='flex'
        document.querySelector('div[class="no-items"]').style.display='none'
    }
    
    const divpay = document.getElementById('paycont')
    divpay.innerHTML=`
    <textarea name="note" id="" cols="30" rows="5" placeholder="Add note to your order" ></textarea>
    `
     //   
    cartListDis.forEach((elt)=>{
        const inputP = document.createElement('input');
        inputP.type = 'hidden';
        inputP.name = 'product_id[]';
        inputP.value = elt.idProd;
        const inputQ = document.createElement('input');
        inputQ.type = 'hidden';
        inputQ.name = 'product_q[]';
        inputQ.value = parseInt(elt.quan, 10);
        console.log(elt.quan)
        divpay.appendChild(inputP);
        divpay.appendChild(inputQ);
    })
    //
    

   
}



// document.querySelector('.pay-btn').addEventListener('click',()=>{
//     localStorage.clear()
// })
categories.addEventListener('click',(e)=>{
    categories.classList.toggle('categoriesnav')
    document.querySelector('ul.submenu').classList.toggle('displaylist')
})
const displayCartBtn = document.querySelector('li[class="nav-elt rounded-cart"]')
const cartContainer = document.querySelector('.cart-area')
displayCartBtn.addEventListener('click',displayCartList)
document.querySelector('.close-cart').addEventListener('click',()=>{
    cartContainer.style.display='none'
    const cartElt = document.getElementById('cart-item-nbr')
    let cartListDis=JSON.parse(localStorage.getItem('cartList'))
    if(cartListDis && cartListDis.length!=0){
    		cartElt.classList.add('cart-item-nbr')
    		cartElt.textContent=cartListDis.length
    }else{
        cartElt.classList.remove('cart-item-nbr')
    	cartElt.textContent=''
    }
  
})
document.getElementById('cart-items')
