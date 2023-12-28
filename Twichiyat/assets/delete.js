const container = document.querySelector('.dashboard-container')
const deleteBtn = document.querySelector('a[name="Delete_Account"]')
const deleteMessage = document.querySelector('div[class="delete hidden-div"]')
const cancelBtn = document.querySelector('button[class="btn-elet cancel"]')
deleteBtn.addEventListener('click',()=>{
    deleteMessage.classList.toggle('hidden-div')
    container.style.opacity=0.6
})
cancelBtn.addEventListener('click',CancelFun)
function CancelFun(e){
    console.log('cansel')
    location.reload()
}