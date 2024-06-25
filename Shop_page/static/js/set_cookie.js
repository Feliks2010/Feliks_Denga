const buttonsBuy = document.querySelectorAll(selectors = ".buy")

for (let count = 0; count < buttonsBuy.length; count++){
    let button = buttonsBuy[count]
    button.addEventListener(
        type = "click",
        listener = function(event) {
            if (document.cookie != ""){
                let current_product = document.cookie.split("=")[1]
                let id_product = current_product + " " + button.id
                document.cookie = `product = ${id_product}; path = /`
                window.location.reload()
            }

            else{
                document.cookie = `product = ${button.id}; path = /`
            }
        }
    )
}


const classProduct = document.querySelectorAll(".product")
for(let count = 0; count< classProduct.length; count++){
    let price = classProduct[count].querySelector(".price")
    let price1 = price.innerHTML.split(" ")[0]
    let discount = classProduct[count].querySelector(".discount")
    let discount1 = discount.innerHTML.split(" ")[1].split("%")[0]

    price.innerHTML = Math.floor(Number(price1 - price1 * discount1 / 100)) + " грн"
}
let clickCount = 0; 
       
function incrementCounter() { 
    clickCount++; 
    document.getElementById('counter').innerHTML = clickCount; 
    let header = document.getElementById('counter'); 
    console.log(header.innerHTML) 
 
    const counterElement = document.getElementById('counter'); 
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
cookie = document.cookie

for (let count = 0; count < cookie.split(" ").length; count ++){
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