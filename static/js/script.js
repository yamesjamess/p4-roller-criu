// This function is to close the alert box after 5 seconds
$(document).ready(function() {
    setTimeout(function() {
        let message = $('#msg');
        let alert = new bootstrap.Alert(message);
        alert.close();
    }, 5000);
});