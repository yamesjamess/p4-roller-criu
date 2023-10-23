$(document).ready(function() {
    setTimeout(function() {
        let message = $('#msg');
        let alert = new bootstrap.Alert(message);
        alert.close();
    }, 5000);
});