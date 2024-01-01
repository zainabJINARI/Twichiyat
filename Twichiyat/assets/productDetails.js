const container =document.querySelector('section[class="new-products-list margin"]')
const inputq = document.getElementById('valueQuant');
inputq.value=1
let quant
let cartArray=[]
var idP=1
let cartList=JSON.parse(localStorage.getItem('cartList'))
const addCarBtn = document.getElementById('add-cart')
const cartElt = document.getElementById('cart-item-nbr') 
if(cartList && cartList.length!=0){
	cartElt.classList.add('cart-item-nbr')
	cartElt.textContent=cartList.length
}
//const cartNbr = document.getElementById('cart-item-nbr')
//cartNbr.textContent=2

addCarBtn.addEventListener('click',()=>{
	console.log(cartList)
    newItem={
		idProd:parseInt(idP, 10),
		name:document.getElementById("modalProductName").innerHTML,
		price:document.getElementById("modalProductPrice").innerHTML,
		size:document.getElementById("size").innerHTML,
		img:document.getElementById("modalImage").src,
		desc:document.getElementById("description").innerHTML,
		quan:inputq.value,
		maxquant:quant
	}
	if(!cartList){
		localStorage.setItem('cartList',JSON.stringify([newItem]))
		cartElt.classList.add('cart-item-nbr')
		cartElt.textContent=1
	}else{
		console.log('here')
		const containsItem = cartList.some(item => item.name === newItem.name);
		if(containsItem){
			console.log('already in there ')
			//if the movie is already in the watchlist
			return
		}else{
			cartList.unshift(newItem)
			localStorage.setItem('cartList',JSON.stringify(cartList))
			cartElt.classList.add('cart-item-nbr')
			cartElt.textContent=cartList.length
			
		}
	}
	
})
function showProductModal(name, price, imageUrl,Quantity=1,description,size,id) {
				quant = Quantity
				idP=id
				console.log(idP)
				document.getElementById("modalImage").src = imageUrl;
				document.getElementById("modalProductName").innerHTML = "Product: " + name;
				document.getElementById("modalProductPrice").innerHTML = "Price :"+price + " $";
				document.getElementById("size").innerHTML= "Available size:"+size
				document.getElementById("description").innerHTML="description:"+description 
				document.getElementById("quantity").innerHTML="Hurry Up We Still Have Just: "+Quantity+" item"
				document.getElementById("productModal").style.display = "block";
                document.querySelector(".modal-content").style.display="flex"
				
				
			}
			function add(){
				console.log(quant)
				let currentValue = parseInt(inputq.value, 10) || 0;
                // Parse the current value as an integer (or default to 0)
                
				if (quant>currentValue){
                    inputq.value = currentValue + 1; 
                }
				 // Increment the value by one and set it back
			};
            function sub(){
                let currentValue = parseInt(inputq.value, 10) || 0; 
                if (currentValue>1){
                    inputq.value = currentValue - 1; 
                }
            }
			function closeProductModal() {
                inputq.value=1
				document.getElementById("productModal").style.display = "none";
                document.querySelector(".modal-content").style.display="none"
				
			}