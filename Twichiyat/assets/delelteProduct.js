const deleteBtn = document.querySelector('a[name="Delete_Product"]');
const deleteMessage = document.querySelector('div[class="delete hidden-div"]');
const cancelBtn = document.querySelector('button[class="btn-elet cancel"]');
const tr_product= document.querySelectorAll(".tr_product");
const deleteForm = document.getElementById('deleteForm');

tr_product.forEach(item => {
    item.addEventListener('click', function () {
        item.classList.toggle('selected-item');
    });
});



deleteBtn.addEventListener('click', () => {
    deleteMessage.classList.toggle('hidden-div');
    body.style.opacity = 0.6;
});

cancelBtn.addEventListener('click', CancelFun);
function CancelFun(e) {
    body.style.opacity = 1;
    console.log('cancel');
    location.reload();
}


deleteForm.addEventListener('click', (e) => {

    e.preventDefault();
    const selectedIds = [];
    const selectedProducts = document.querySelectorAll('.selected-item');

    selectedProducts.forEach(Product => {
        const productId = Product.querySelector('.product-id').textContent;
        selectedIds.push(productId);
    });

    selectedIds.forEach(id => {
      const input = document.createElement('input');
      input.type = 'hidden';
      input.name = 'selected_ids[]';
      input.value = id;
      deleteForm.appendChild(input);
    });
    deleteForm.submit();
});