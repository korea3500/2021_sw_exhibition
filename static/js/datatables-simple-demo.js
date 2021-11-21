// window.addEventListener('DOMContentLoaded', event => {
//     // Simple-DataTables
//     // https://github.com/fiduswriter/Simple-DataTables/wiki

//     const datatablesSimple = document.getElementById('datatablesSimple');
//     if (datatablesSimple) {
//         new simpleDatatables.DataTable(datatablesSimple);
//     }
// });

$(document).ready(function() {
    var table = $("#datatablesSimple").DataTable({
        dom : 'Bfrtip',
        buttons : [
           'copy', 'excel'
        ]
    });
    $('#datatablesSimple_filter').prepend('<label><select id="select" type = "search" class placeholder aria-controls="databaseSimple"></select></label>');
    $('#datatablesSimple > thead > tr').children().each(function (indexInArray, valueOfElement) { 
        $('#select').append('<option>'+valueOfElement.innerHTML+'</option>');
    });
    $('.dataTables_filter input').unbind().bind('keyup', function () {
        var colIndex = document.querySelector('#select').selectedIndex;
        table.column(colIndex).search(this.value).draw();
    });



})