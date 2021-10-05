var csrftoken = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function () {
    // Create save timer


    $("#about-btn").click(function (event) {
        alert("You clicked the button using JQuery!");
    });

    $(".card").hover(function () {
            $(this).addClass('alert-danger');
        },
        function () {
            $(this).removeClass('alert-danger');
        });

});