//  Знаходимо об'єкт по класу
const buttonsBuy = document.querySelectorAll(selectors = ".buy")
// Перебираємо всі наші кнопки
for (let count = 0; count < buttonsBuy.length; count++){
    // Обращаємось до певної кнопки
    let button = buttonsBuy[count]
    // Додаємо слухач кліку на кнопку
    button.addEventListener(
        // Вказуємо тип події
        type = "click",
        // Створюємо функцію
        listener = function(event) {
            // Якщо cookie не пусті
            if (document.cookie != ""){
                // Дізнаємося теперешній товар
                let current_product = document.cookie.split("=")[1]
                // Створюємо id
                let id_product = current_product + " " + button.id
                // Записуємо в cookie id товару
                document.cookie = `product = ${id_product}; path = /`
                // Перезавантаження сторінки
                window.location.reload()
            }
            // Інакше
            else{
                // Записуємо в cookie id кнопки
                document.cookie = `product = ${button.id}; path = /`
            }
        }
    )
}
// Знаходимо по класу об'єкти
const classProduct = document.querySelectorAll(".product")
// Перебираємо кожний об'єкт
for(let count = 0; count< classProduct.length; count++){
    // Створюємо змінну, де храниться ціна товару
    let price = classProduct[count].querySelector(".price")
    // Беремо ціну з сайту
    let price1 = price.innerHTML.split(" ")[0]
    // Дізнаємося знижку
    let discount = classProduct[count].querySelector(".discount")
    // Дізнаємося знижку, яка на сайті
    let discount1 = discount.innerHTML.split(" ")[1].split("%")[0]
    // Перезапизуємо ціну з врахуванням знижки
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