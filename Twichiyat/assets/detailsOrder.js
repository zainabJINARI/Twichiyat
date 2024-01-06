function showProductDetailsAlert(address, city, postalCode, note) {
    
    var detailsContent = `
        <h3>Order Details</h3>
        <div>
            <p>Address: <span>${address}</span></p>
            <p>City: <span>${city}</span></p>
            <p>Postal Code: <span>${postalCode}</span></p>
            <p>Note: <span>${note}</span></p>
        </div>   
    `;

    let detailsDiv = document.getElementById('productDetails');
    detailsDiv.style.display="flex"
    detailsDiv.innerHTML=""
    const closebnt = document.createElement('span')
    closebnt.innerHTML='&times;'
    
    detailsDiv.innerHTML += detailsContent;
    detailsDiv.appendChild(closebnt)
    closebnt.addEventListener('click',()=>{
        console.log('you clocked me')
        detailsDiv.style.display="none"
    })
    
    detailsDiv.classList.remove('hidden-div');
}