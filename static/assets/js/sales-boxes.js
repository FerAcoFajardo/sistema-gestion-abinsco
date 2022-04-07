const box_credit = document.getElementById('payment-method-block');
const box_options = document.getElementById('credit-options-block');

function handleRadioClick() {
    if (document.getElementById('credito').checked) {
        if(document.getElementById("payment")) {
            removeElement();    
        } 
    } else {
        if(!document.getElementById("payment")) {
            addElement();    
        }        
    }
}

const radioButtons = document.querySelectorAll('input[name="tipo"]');
radioButtons.forEach(radio => {
    radio.addEventListener('click', handleRadioClick);
});

function addElement() {

    // Crea el div del método de pago
    var newDiv = document.createElement("div");
    newDiv.setAttribute("id", "payment");
    var content = `
        <p>Método de pago:</p>
            
        <div id="radios">
            <input type="radio" id="efectivo" name="metodo" value="Efectivo" checked />
            <label for="efectivo">Efectivo</label>
        </div>
        <div id="radios">
            <input type="radio" id="tarjeta" name="metodo" value="Tarjeta" />
            <label for="tarjeta">Tarjeta</label>
        </div>
        `
    newDiv.innerHTML = content; 

    var currentDiv = document.getElementById("payment-method-block");
    currentDiv.appendChild(newDiv);

    // Elimina el div de los detalles del credito (si se hara un primer abono)
    var currentDiv = document.getElementById("credit-details");

    while(currentDiv.firstChild) {
        currentDiv.removeChild(currentDiv.firstChild);
    }
  }

  function removeElement() {
    // Elimina el div del método de pago
    var currentDiv = document.getElementById("payment-method-block");

    while(currentDiv.firstChild) {
        currentDiv.removeChild(currentDiv.firstChild);
    }

    // Agrega el div de los detalles del credito (si se hara un primer abono)
    var newDiv = document.createElement("div");
    newDiv.setAttribute("id", "credit");
    var content = 
        `
        <div class="row mb-5">
            <div class="col-md-12">
                <div  id="estilo-tabla" class="pb-2">  
                        <h2 id="titulo">Registrar primer abono</h2>
                        <div id="credit-first-payment">
                            <p>¿Desea realizar un abono?:</p>
                            <div id="radios">
                                <input type="radio" id="no" name="primer-pago" value="no" checked />
                                <label for="no">No</label>
                            </div>
                            <div id="radios">
                                <input type="radio" id="si" name="primer-pago" value="si" />
                                <label for="si">Si</label>
                            </div>
                        </div>
                        <div id="payment-method-credit">
                            <p>Método de pago:</p>
                            <div id="radios">
                                <input type="radio" id="efectivo" name="metodo-abono" value="Efectivo" checked />
                                <label for="efectivo">Efectivo</label>
                            </div>
                            <div id="radios">
                                <input type="radio" id="tarjeta" name="metodo-abono" value="Tarjeta" />
                                <label for="tarjeta">Tarjeta</label>
                            </div>
                        </div>
                        
                        <dl>
                            <dt>Total a abonar:</dt>
                            <dd>
                                <div class="d-flex flex-column bd-highlight mx-auto">
                                <input type="number" class="form-control" name="amount-payment" value="0" min="0" id="total-payment" />
                                </div>
                            </dd>
                        </dl>
                </div>
            </div>
        </div>
        `
    newDiv.innerHTML = content; 

    var currentDiv = document.getElementById("credit-details");
    currentDiv.appendChild(newDiv);
  }

