
var timer;
var saved = false;
function myTimer(){
    var sec = 15;
    clearInterval(timer);
    timer = setInterval(function() {
        if(saved === false)
        {
            console.log("Timer tripped");
            console.log($("#id_textresponse").val())
            saved = true;
        }

    },5000);
}


$(document).ready(function () {

    $("#my-ajax-button").click(function(event){
        event.preventDefault();
        $.post('/retranslation/ajax-test/',
            {
                id:'{{ program.programName|capfirst }}',
                action:'We was actions and stuff'
            });

    });

    $("#id_textresponse").on('input',function(){
        console.log("We changed");
        saved = false;
        myTimer();
    });

});