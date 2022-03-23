

function removeCartItem(event) {
    var buttonClicked = event.target
    buttonClicked.parentElement.parentElement.remove()
    updateCartTotal()
}

function quantityChanged(event) {
    var input = event.target
    if (isNaN(input.value) || input.value <= 0) {
        input.value = 1
    }
    updateCartTotal()
}

function addToCartClicked(event) {
    var button = event.target
    var shopItem = button.parentElement.parentElement
    var title = shopItem.getElementsByClassName('shop-item-title')[0].innerText
    var price = shopItem.getElementsByClassName('shop-item-price')[0].innerText
    var imageSrc = shopItem.getElementsByClassName('shop-item-image')[0].src
    addItemToCart(title, price, imageSrc)
    updateCartTotal()
}

let button = document.getElementById('add-form')

button.addEventListener("click", () => {
    let product = document.getElementById('id_form-product')
    $.ajax({
        url: `http://localhost:8000/sales/get_product/${product.value}`,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            addItemToCart(data.id, data.name, data.price, data.image)
        }
    });
});

function addItemToCart(id, title, price, imageSrc) {
    var cartRow = document.createElement('tr')
    // cartRow.classList.add('cart-row')
    var cartItems = document.querySelector('#cart-body')
    var cartItemNames = cartItems.getElementsByClassName('cart-item-title')
    for (var i = 0; i < cartItemNames.length; i++) {
        if (cartItemNames[i].innerText == title) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Ya agregaste ese producto!'
            })
            return
        }
    }


    let total_form = document.querySelector('#id_form-TOTAL_FORMS')

    var cartRowContents = `
            <td class="cart-item  cart-column align-middle">
                <img class="img-fluid cart-item-image " src="${imageSrc}" width="30" height="30">
                <input type="hidden" name="form-${total_form.value}-product" class="cart-item-title" id="id_form-${total_form.value}-product" value="${id}"><span class="cart-item-title">${title}</span>
            </td>

            <td class="center-block align-middle">
                    <input type="text" name="form-${total_form.value}-price" value="0" readonly class="cart-price" id="id_form-${total_form.value}-price">
            </td>

            <td class="cart-quantity align-middle">
                
                <input type="number" name="form-${total_form.value}-amount" class="cart-quantity-input" min="1" value="1" id="id_form-${total_form.value}-amount">
            </td>

            <td class="cart-column align-middle">    
                <input type="number" name="form-${total_form.value}-total" readonly class="product-total" id="id_form-${total_form.value}-total">
                <a class="btn btn-danger btn-sm" type="button"><i class="fas fa-trash-alt"></i></a>
            </td>`

            /*
                
                <a class="btn btn-danger btn-sm" type="button"><i class="fas fa-trash-alt"></i></a>
            */

    cartRow.innerHTML = cartRowContents
    cartRow.querySelector('.cart-price').value = price
    cartRow.querySelector(`#id_form-${total_form.value}-product`).value = id
    cartItems.append(cartRow)
    let amount = cartRow.querySelector(`#id_form-${total_form.value}-amount`)
    cartRow.querySelector(`#id_form-${total_form.value}-total`).value = price * amount.value
    cartRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeCartItem)
    cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', quantityChanged)
    // Add event listener for quantity input
    total_form.value = parseInt(total_form.value) + 1
    updateCartTotal()
}



function updateCartTotal() {
    var table_length = document.getElementById("cart-table").rows.length
    var total = 0

    for (i = 0; i < table_length - 1; i++) {
        var priceElement = document.getElementById(`id_form-${i}-price`)
        var quantityElement = document.getElementById(`id_form-${i}-amount`)
        var itemTotal = document.getElementById(`id_form-${i}-total`)

        console.log(`precio: ${priceElement.value}`)
        console.log(`cantidad: ${quantityElement.value}`)
        console.log(`total: ${itemTotal.value}`)

        var price = parseFloat(priceElement.value)
        itemTotal.value = price * quantityElement.value
        total +=  parseFloat(itemTotal.value)
    }
    total = Math.round(total * 100) / 100
    document.getElementById('id_total').value = total
}