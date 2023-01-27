
/**
 * Logik des Postens
 */
$('#post-modal').on('shown.bs.modal', function () {
    $('#post-text').trigger('focus');
})

$('#post-icon').click(function(event){
    $('#post-modal').show();
})

$('#post-button').click(function(event){
    
    var benutzer = localStorage.getItem('benutzer')
    var zeit = Math.round(Date.now() / 1000)
    var text = $('#post-text').val();
    $.ajax('/api/post', {
        data : JSON.stringify({"benutzer": benutzer, "zeit": zeit, "text": text}),
        contentType : 'application/json',
        type : 'POST'
    });
    $('#post-modal').hide();
})

$('#post-close-button').click(function(event){
    $('#post-modal').hide();
})