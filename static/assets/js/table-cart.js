

function removeCartItem(event) {
    let buttonClicked = event.currentTarget
    console.log('Button id '+buttonClicked.id)
    
    
    let total_form = document.querySelector('#id_form-TOTAL_FORMS')
    // Iterate through all the forms
    for (i = 0; i < total_form.value; i++) {
        if(i >= buttonClicked.id){
            // Get the amount
            let amount = document.getElementById(`id_form-${i}-amount`)
            console.log("i value: " + i)
            console.log(amount)
            // Get the price
            let price = document.getElementById(`id_form-${i}-price`)
            // Get the total
            let total = document.getElementById(`id_form-${i}-total`)
            // Get the discount
            let discount = document.getElementById(`id_form-${i}-discount`)
            // Get product
            let product = document.getElementById(`id_form-${i}-product`)
            
            // Changes the IDs
            amount.id = `id_form-${i-1}-amount`

            price.id = `id_form-${i-1}-price`
            total.id = `id_form-${i-1}-total`
            discount.id = `id_form-${i-1}-discount`
            product.id = `id_form-${i-1}-product`
            // Change the names
            amount.name = `form-${i-1}-amount`
            price.name = `form-${i-1}-price`
            total.name = `form-${i-1}-total`
            discount.name = `form-${i-1}-discount`
            product.name = `form-${i-1}-product`
            buttonClicked.id = i-1
            
        }
    }
    buttonClicked.parentElement.parentElement.remove()
    total_form.value = parseInt(total_form.value) - 1
    updateCartTotal()
}

function quantityChanged(event) {
    var input = event.target
    if (isNaN(input.value) || input.value <= 0) {
        input.value = 1
    }
    updateCartTotal()
}

function priceChanged(event) {
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
    var description = shopItem.getElementsByClassName('shop-item-description')[0].innerText
    var code = shopItem.getElementsByClassName('shop-item-code')[0].innerText
    var unity = shopItem.getElementsByClassName('shop-item-unity')[0].innerText
    var imageSrc = shopItem.getElementsByClassName('shop-item-image')[0].src
    addItemToCart(title, price, imageSrc, description, code, unity)
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
            console.log(data)
            addItemToCart(data.id, data.name, data.price, data.image, data.stock, data.description, data.code, data.unity, data.category_id)
        }
    });
});

function addItemToCart(id, title, price, imageSrc, stock, description, code, unity, category_id) {
    var cartRow = document.createElement('tr')
    // cartRow.classList.add('cart-row')
    var cartItems = document.querySelector('#cart-body')
    var cartItemNames = cartItems.getElementsByClassName('cart-item-title')
    for (var i = 0; i < cartItemNames.length; i++) {
        if (cartItemNames[i].innerText == description) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Ya agregaste ese producto!'
            })
            return
        }
    }

    /*
        'id': product.id,
        'name': product.name,
        'price': product.current_price,
        'stock': product.in_storage,
        'image': product.image.url,
        'description': product.description,
        'code': product.code,
        'unity': product.unity,
        'category_id': product.category_id
    */ 


        /*
            <th>Código</th>
            <th>Cantidad</th>
            <th>Unidad</th>
            <th>Descripción</th>
            <th>Precio</th>
            <th>Descuento</th>
            <th>Total</th>
        */

    let total_form = document.querySelector('#id_form-TOTAL_FORMS')

    var cartRowContents = `

            <td class="cart-item  cart-column align-middle text-center">
                <input type="hidden" name="form-${total_form.value}-code" class="cart-item-code" id="id_form-${total_form.value}-code" value="${id}"><span class="cart-item-code">${code}</span>
            </td>

            <td class="cart-quantity align-middle text-center">
                <input type="number" name="form-${total_form.value}-amount" class="cart-quantity-input" min="1" value="1" id="id_form-${total_form.value}-amount">
            </td>

            <td class="cart-item  cart-column align-middle text-center">
                <input type="hidden" name="form-${total_form.value}-unity" class="cart-item-unity" id="id_form-${total_form.value}-unity" value="${id}"><span class="cart-item-unity">${unity}</span>
            </td>

            <td class="cart-item  cart-column align-middle">
                <input type="hidden" name="form-${total_form.value}-product" class="cart-item-title" id="id_form-${total_form.value}-product" value="${id}"><span class="cart-item-title">${description}</span>
            </td>

            <td class="center-block align-middle text-center">
                    <input type="number" name="form-${total_form.value}-price" value="0" class="cart-price" id="id_form-${total_form.value}-price">
            </td>

            <td class="cart-discount align-middle text-center">
                <input type="number" name="form-${total_form.value}-discount" class="cart-quantity-input" min="0" value="0" id="id_form-${total_form.value}-discount">
            </td>

            <td class="cart-column align-middle text-center">    
                <input type="number" name="form-${total_form.value}-total" readonly class="product-total" id="id_form-${total_form.value}-total">
            </td>

            <td class="cart-column align-middle text-center">
                <a class="btn btn-danger btn-sm" id=${total_form.value} type="button"><i class="fas fa-trash-alt"></i></a>
            </td>`


    cartRow.innerHTML = cartRowContents
    let priceInput = cartRow.querySelector('.cart-price')
    priceInput.value = price
    priceInput.addEventListener('change', priceChanged)
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

const btn_guardar = document.getElementById('submit-btn');

btn_guardar.onclick = function(event){
    let total_form = document.querySelector('#id_form-TOTAL_FORMS')

    if (total_form.value <= 0) {
        event.preventDefault()
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Debes agregar al menos  un producto!'
        })
        return
    }
}

function updateCartTotal() {
    var table_length = document.getElementById("cart-table").rows.length
    var total = 0

    for (i = 0; i < table_length - 1; i++) {

        var priceElement = document.getElementById(`id_form-${i}-price`)
        var quantityElement = document.getElementById(`id_form-${i}-amount`)
        var itemTotal = document.getElementById(`id_form-${i}-total`)
        var itemDiscount = document.getElementById(`id_form-${i}-discount`)

        console.log(`discount: ${itemDiscount.value}`)
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