/**
 * Fake Login eines Nutzers
 */

$('#login-modal').on('shown.bs.modal', function () {
    $('#login-input').trigger('focus');
})

$('#user-icon').click(function(event){
    $('#login-modal').show();
})

$('#login-button').click(function(event){
    var benutzer = $('#login-input').val();
    localStorage.setItem('benutzer', benutzer);
    console.log(localStorage.getItem('benutzer'));
    $('#login-modal').hide();
})

$('#login-close-button').click(function(event){
    $('#login-modal').hide();
})
