const pricetotal = document.querySelector('.total-price')
let cartListDis=JSON.parse(localStorage.getItem('cartList'))
let sum=0
cartListDis.forEach(element => {
    sum += parseInt(element.price .match(/\b\d+\b/) || 0) * parseInt(element.quan) ;
});
pricetotal.textContent=sum+"$"

document.querySelector('button[type="submit"]').addEventListener('click',()=>{
    console.log('you clicked me ')
    localStorage.clear()
})