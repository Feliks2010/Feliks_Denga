// function funcplus(button) {
//     let productDiv = button.closest('.product');
//     let countElement = productDiv.querySelector('.product_count');
//     let count = parseInt(countElement.innerText, 10);
//     count += 1;
//     countElement.innerText = count;
// }

// function funcminus(button) {
//     let productDiv = button.closest('.product');
//     let countElement = productDiv.querySelector('.product_count');
//     let count = parseInt(countElement.innerText, 10);
//     count -= 1;
//     countElement.innerText = count;
// }
const listButtonsMinus = document.querySelectorAll(".minus");

for (let count = 0; count < listButtonsMinus.length; count++) {
    let button = listButtonsMinus[count];
    button.addEventListener("click", function(event) {
        let cookies = document.cookie.split("=")[1].split(" ");
        let button_id = button.id.split("-")[1];
        
        // Перевірка наявності button_id в cookies
        if (cookies.includes(button_id)) {
            // Видалення button_id з cookies
            cookies.splice(cookies.indexOf(button_id), 1);
            // Зменшення значення наступного елемента
            button.nextElementSibling.textContent = Number(button.nextElementSibling.textContent) - 1;
        }

        // Видалення продукту, якщо значення стало 0
        if (button.nextElementSibling.textContent === '0') {
            document.querySelector(`#product-${button_id}`).remove();
        }
        
        // Оновлення cookies
        document.cookie = `product=${cookies.join(' ')}; path=/`;
    });
}

// function funcPlus(button){
//     let product = button.closest('.product');
//     let countElement = product.querySelecter('.product_count');
//     let count = parseInt(countElement.innerText, 10);
//     count += 1 
//     countElement.innerText = count
// }
// function funcMinus(button){
//     let product = button.closest('.product');
//     let countElement = product.querySelecter('.product_count');
//     let count = parseInt(countElement.innerText, 10);
//     count -= 1 
//     countElement.innerText = count
// }