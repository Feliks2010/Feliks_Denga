function reload(){
    window.location.reload();
}
cookie = document.cookie
const listButtonsMinus = document.querySelectorAll(".minus");
const listAllPrice = document.querySelectorAll(".price");
const listAllCount = document.querySelectorAll(".product_count");
const allPrice = document.querySelector(".allPrice")

for (let count = 0; count < listButtonsMinus.length; count++) {
    // allPrice.innerHTML = Number(classProduct[count].querySelector(".price").innerHTML.split(" ")[0]) * Number(listAllCount[count].innerHTML) + " грн"

    let button = listButtonsMinus[count];
    let countProductElement = listAllCount[count];
    
    button.addEventListener("click", function(event) {
        let cookies = document.cookie.split("=")[1].split(" ");
        let button_id = button.id.split("-")[1];

        if (cookies.includes(button_id)) {
            cookies.splice(cookies.indexOf(button_id), 1);
            countProductElement.textContent = Number(countProductElement.textContent) - 1;
            reload()
        }
        
        if (countProductElement.textContent == "0") {
            document.querySelector(`#product-${button_id}`).remove();
        }
        
        document.cookie = `product=${cookies.join(" ")}; path=/`;
    });

}


const listButtonsPlus = document.querySelectorAll(".plus")

for(let count = 0; count <  listButtonsPlus.length; count++){
    let button_plus = listButtonsPlus[count]
    let button_minus = listButtonsMinus[count]

    button_plus.addEventListener(
        type = "click", 
        listener = function(
            event
        ){
            let cookies = document.cookie.split("=")[1].split(" ")
            let button_id = button_plus.id.split("-")[1]
            let current_product = document.cookie.split("=")[1]
            let id_product = current_product + " " + button_id
            // document.cookie = `${id_product};path = /`
            listAllCount[count] = listAllCount[count] + 1

            if (button_id in cookies || cookies == button_id){
                cookies.splice(cookies.indexOf(button_id), 1)
                button_minus.previousElementSibling.textContent = Number(button_minus.previousElementSibling.textContent) + 1
                reload()
            }

            document.cookie = `product=${id_product}; path = /` 
        }
    )
}

const classProduct = document.querySelectorAll(".product");
let totalSum = 0
let totalCount = 0
let totalDiscount = 0
let totalSumWithoutDiscount = 0


for (let count = 0; count < classProduct.length; count++) {

// Припускаючи, що у кожного продукту є елемент з класом "price"
    let price = classProduct[count].querySelector(".price");
    let priceWithoutDiscount = classProduct[count].querySelector(".price").innerHTML;
    let price1 = price.innerHTML.split("г")[0]
    let discount = classProduct[count].querySelector(".discount");
    let discount1 = discount.innerHTML.split(" ")[1].split("%")[0]

    console.log(Number(price1 - price1 * discount1 / 100))
    price.innerHTML = Math.floor(Number(price1 - price1 * discount1 / 100)) + " грн"
    discountedPrice = Number(price.innerHTML.split("г")[0])
    allPrice.innerHTML = discountedPrice
    totalSum += Math.floor(discountedPrice) * listAllCount[count].innerHTML;
    totalCount += Number(listAllCount[count].innerHTML)
    let discount2 = Number(price1 * discount1 / 100)
    totalDiscount += Math.floor(Number(discount2 * listAllCount[count].innerHTML))
    totalSumWithoutDiscount += Math.floor(Number(priceWithoutDiscount.split("г")[0] * listAllCount[count].innerHTML))

allPrice.innerHTML = totalSum + " грн";
document.querySelector(".allCount").innerHTML = totalCount + "-и товари на суму"
document.querySelector(".allDiscount").innerHTML =totalDiscount + " грн"
document.querySelector(".allPriceWithoutDiscount").innerHTML = totalSumWithoutDiscount + " грн"
}
// const allCount = document.querySelector(".allCount")

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

const design = document.querySelector("#buy")
design.addEventListener(
    type = "click",
    listener = (event) => {
        document.querySelector(".frame-cart").style.display = "flex"

    } 
)
