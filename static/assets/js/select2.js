$('#id_customer').on('select2:select', function (e) { 
    //var customerSelected = $('#id_customer').select2('data')
    var customerSelected = e.params.data.id;
    $.ajax({
        url: `http://localhost:8000/sales/get_customer_by_id/${customerSelected}`,
        type: 'GET',
        dataType: 'json'
    }).done(function( data2 ) {
        document.getElementById('customer-name').innerHTML = data2.name
        document.getElementById('customer-rfc').innerHTML = data2.rfc
        document.getElementById('customer-address').innerHTML = data2.address
        document.getElementById('customer-phone').innerHTML = data2.phone
        document.getElementById('customer-email').innerHTML = data2.email
    })
});

$("#id_customer").select2({
    ajax: {
        url: `http://localhost:8000/sales/get_customers_by_name`,
        type: 'GET',
        dataType: 'json',
        processResults: function (data) {
            // Transforms the top-level key of the response object from 'items' to 'results'
            var dataObject = JSON.parse(data)
            return {
                
                results: dataObject
            };
        }
        // Additional AJAX parameters go here; see the end of this chapter for the full code of this example
    }
});

$("#id_form-product").select2({
    ajax: {
        url: `http://localhost:8000/sales/get_products_by_name`,
        type: 'GET',
        dataType: 'json',
        processResults: function (data) {
            var dataObject = JSON.parse(data)
            // Transforms the top-level key of the response object from 'items' to 'results'
            return {
                results: dataObject
            };
        }
        // Additional AJAX parameters go here; see the end of this chapter for the full code of this example
    }
});
