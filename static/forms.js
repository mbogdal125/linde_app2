
/*jslint browser: true*/
/*global $, jQuery, autofillInsertSheet, clearTimeout, document, getSheetInfo, selectBoxWithValue, setTimeout, checkClientNumber, getIdWithDelay, setName, displayCustomerInfo */
'use strict';

$(document).ready(function() {
    checkClientNumber();
    autofillInsertSheet();
});


function autofillInsertSheet() {
    var insertNode = $('.insert_sheet_form'), timeoutObject = null;
    if (insertNode.length) {
        $('form.insert-stock-data-form').keypress(getIdWithDelay);

    }
    function getIdWithDelay() {
        clearTimeout(timeoutObject);
        timeoutObject = setTimeout(setName, 1000);
        function setName() {
            getSheetInfo($("#id_stock_sheet_number").val());

        }
    }
}

function getSheetInfo(sheet_number) {
    $.ajax({
        url: configuration["linde_app"]["autofill-sheet"],
        cache: false,
        type: "POST",
        data: {sheet_number: sheet_number},
        success: displayCustomerInfo,
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        }
    });
    function displayCustomerInfo(data) {
        $('.sheet_info').text(data.status + " " + data.sheet_data.customer_number + " " + data.sheet_data.stocktaking_id + " " + data.sheet_data.stocktaking_date);
        selectBoxWithValue('id_id_customer', data.sheet_data.customer_number);
        selectBoxWithValue('id_id_stocktaking', data.sheet_data.stocktaking_id);
        document.getElementById("id_notes").value = data.sheet_data.notes;
        document.getElementById("id_stockTakingDate").value = data.sheet_data.stocktaking_date;


    }


}

function selectBoxWithValue(field_id, value) {
    var options_values = document.getElementById(field_id).children;
    var options = document.getElementById(field_id).children.length;


    for (var x=0; x < options; x++) {

        if (options_values[x].text == value) {
            console.debug(options_values[x]);
            //options_values[x].setAttribute("selected", "selected");
            options_values[x].selected = "selected";
        }
    }

}

function checkClientNumber() {

    var searchNode = $('.search-insert');
    var timeoutObject = null;

    if(searchNode.length){
        $('form.search-insert-form').keypress(getIdWithDelay);

    }


    function getIdWithDelay() {
        clearTimeout(timeoutObject);
        timeoutObject = setTimeout(setName, 1000);
        function setName() {
            console.debug($("#id_search_field").val());
            getClientInfo($("#id_search_field").val());
            console.debug($("#id_search_field").val());
        }

    }

}



function getClientInfo(client_id) {
    $.ajax({
        url: configuration["linde_app"]["fill-sheet-data"],
        cache: false,
        type: "POST",
        data: {client_id: client_id},
        success: displayCustomerInfo,
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        }
    });
    function displayCustomerInfo(data) {

        $('.customer_info').text(data.status + " " + data.customer.number + " " + data.customer.name);

    }

}

