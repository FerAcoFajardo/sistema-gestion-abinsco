

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
