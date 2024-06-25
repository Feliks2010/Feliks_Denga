let cookie = document.cookie

if (cookie){
    for (let count = 0; count < cookie.split('')[1].split(';')[0].split(" ").join("").length; count++){
    let cookie = document.cookie;

    let cookieValue = cookie.split('=')[1].split(';')[0].split(" ").join("");
    

    let length = cookieValue.length;
    
    
    const count_products = document.querySelector('.count_products');
    
    let counterElement = 0
    count_products.textContent = length;
    if (length == 0){
        count_products.style.color = 'white';
    } 

    else {
        count_products.style.position = 'absolute';
        count_products.style.top = '15px';
        count_products.style.left = '475px';
        count_products.style.width = '35px';
        count_products.style.height = '35px';
        count_products.style.borderRadius = '50%';
        count_products.style.border = '1px solid #000';
        count_products.style.textAlign = 'center';
        count_products.style.display = 'flex';
        count_products.style.justifyContent = 'center';
        count_products.style.alignItems = 'center';
        count_products.style.backgroundColor = '#EFCB4A';
        count_products.style.fontSize = '20px';
        count_products.style.color = "black";

    }
}}
else{
    const count_products = document.querySelector('.count_products');
    
    let counterElement = 0
    count_products.textContent = length;
    count_products.style.color = 'white';
}
let cookies = document.cookie
for (let count = 0; count < cookies.split(" ").length; count ++){
    if (cookie.split(" ") != 'product='){
        document.querySelector('.count_product').innerHTML = cookie.split(" ").length
        const counterElement = document.querySelector('.count_product') 
        counterElement.style.position = 'absolute'; 
        counterElement.style.top = '15px'; 
        counterElement.style.left = '475px'; 
        counterElement.style.width = '35px'; 
        counterElement.style.height = '35px'; 
        counterElement.style.borderRadius = '50%'; 
        counterElement.style.border = '1px solid #000'; 
        counterElement.style.textAlign = 'center'; 
        counterElement.style.display = 'flex'; 
        counterElement.style.justifyContent = 'center'; 
        counterElement.style.alignItems = 'center'; 
        counterElement.style.backgroundColor = '#EFCB4A'; 
        counterElement.style.fontSize = '20px'; 
        counterElement.style.color = "black"; 
    }
}