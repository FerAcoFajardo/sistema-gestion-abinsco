

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
        // Check if the input is a float
        input.value = 1
    }
    input.value = Math.floor(input.value)
    updateCartTotal()
}

function priceChanged(event) {
    var input = event.target
    if (isNaN(input.value) || input.value <= 0) {
        input.value = 1
    }
    updateCartTotal()
}
// Crea uno para el descuento mortis Miauuuuuuuu, en lugar de hacer updateProductTotal() te va a tocar hacer una función 
// para actualizar el precio, si, a ver si github copilot tiene ganas de trabajar 
function discountChanged(event) {
    var input = event.target
    if (isNaN(input.value) || input.value <= 0 || input.value > 100 ) {
        input.value = 0
    }
    updateCartTotal()
}

// Function to update product total when discount is changed
function updateProductTotal(index) {
    // Get the discount 
    let discount = document.getElementById(`id_form-${index}-discount`)
    // Get the total
    let total = document.getElementById(`id_form-${index}-total`)
    // Get the price
    let price = document.getElementById(`id_form-${index}-price`)
    // Calculate the new total
    let newTotal = parseFloat(price.value) * (1 - parseFloat(discount.value) / 100)
    // Update the total
    total.value = newTotal.toFixed(2)
    // updateCartTotal()
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
                <input type="number" name="form-${total_form.value}-discount" class="cart-discount-input" min="0" max="100" value="0" id="id_form-${total_form.value}-discount">
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
    // Get discount
    
    cartItems.append(cartRow)
    let amount = cartRow.querySelector(`#id_form-${total_form.value}-amount`)
    cartRow.querySelector(`#id_form-${total_form.value}-total`).value = price * amount.value
    cartRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeCartItem)
    cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', quantityChanged)
    cartRow.getElementsByClassName('cart-discount-input')[0].addEventListener('change', discountChanged)
    total_form.value = parseInt(total_form.value) + 1
    updateCartTotal()
}

function validateStock(){
    // Iterate over all the rows in the table
    let table = document.getElementById('cart-body')
    let rows = table.getElementsByTagName('tr')
    // Iterate over all products in the cart
    for (let i = 0; i < rows.length; i++) {
        let row = rows[i]
        // get the product id
        let product_id = row.querySelector('.cart-item-code').value
        // get the amount
        let amount = row.querySelector('.cart-quantity-input').value
        
        $.ajax({
            url: `http://localhost:8000/sales/get_product/${product_id}`,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                console.log(data)
                if (data.stock < amount) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: `No hay suficiente stock del producto ${data}!`
                    })
                }
            }
        });

    }
}



const btn_guardar = document.getElementById('submit-btn');

btn_guardar.onclick = async function(event){
    var confirmed = false

    event.preventDefault()

    let total_form = document.querySelector('#id_form-TOTAL_FORMS')

    var customer = document.getElementById('id_customer').value

    if (customer == 1 && document.getElementById('credito').checked) {
        
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'A \"venta al publico\" no se le puede asignar credito!'
        })
        return

    } else {
        customer_data = (await fetch(`http://localhost:8000/sales/get_customer_by_id/${customer}`))
        
        data = await customer_data.json();
            
        var actual_deb = data.actual_deb
        var max_credit = data.max_credit
        var total = document.getElementById('id_total').value

        if (max_credit == 0  && document.getElementById('credito').checked) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'El cliente no tiene credito autorizado.'
            })
            return
        }

        if(max_credit > 0 && actual_deb + document.getElementById('id_total').value > max_credit && document.getElementById('credito').checked ) {
            	
                Swal.fire({
                    title: '¿Desea autorizar esta venta?',
                    html: `El cliente ya ha superado su credito!<pre>Credito otorgado: ${max_credit}</pre><pre>Deuda actual: ${actual_deb}</pre><pre>Deuda nueva: ${deb_comprobation}</pre>`,
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Aceptar',
                    cancelButtonText: 'Cancelar',
                  }).then((result) => {
                    if (result.isConfirmed) {
                        $('#sales-form').submit();
                    }
                  })
        } else {
            confirmed = true
        }

        if (total_form.value <= 0) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Debes agregar al menos  un producto!'
            })
            return
        }
        
        if (flag_sale) {
            $('#sales-form').submit();
        }
    }

    if (total_form.value <= 0) {
        event.preventDefault()
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Debes agregar al menos  un producto!'
        })
        return
    }


    if(!document.getElementById('credito').checked) {
        $('#sales-form').submit();
    }

    if(confirmed) {
        $('#sales-form').submit();
    }
}


function updateCartTotal() {
    var table_length = document.getElementById("cart-table").rows.length
    var total = 0

    for (i = 0; i < table_length - 1; i++) {

        var priceElement = document.getElementById(`id_form-${i}-price`)
        var quantityElement = document.getElementById(`id_form-${i}-amount`)
        var itemTotal = document.getElementById(`id_form-${i}-total`)
        var discount = document.getElementById(`id_form-${i}-discount`)
        
        console.log(`precio: ${priceElement.value}`)
        console.log(`cantidad: ${quantityElement.value}`)
        console.log(`total: ${itemTotal.value}`)
        console.log(`descuento: ${discount.value}`)
        
        var price = parseFloat(priceElement.value)
        itemTotal.value = price * quantityElement.value
        // Apply discount
        if (discount.value > 0) {
            itemTotal.value = itemTotal.value - (itemTotal.value * discount.value / 100)
        }


        
        total +=  parseFloat(itemTotal.value)
    }
    total = Math.round(total * 100) / 100
    document.getElementById('subtotal').value = total

    document.getElementById('iva').value = Math.round( (total * 0.16) * 100) / 100

    total = total * 1.16

    

    total = Math.round(total * 100) / 100
    document.getElementById('id_total').value = total
}