
$(function() {
    $('#submit-report-btn').on('click', function(event){
        event.preventDefault();
        console.log("Form Submitted")
        create_bug();
    });

    $('#editButton').on('click', function(event){
        console.log("Some random stuff")
//        editBug(event);
    });

    function create_bug() {
        console.log("create post is working!") // sanity check
        $.ajax({
            url : "create_report/", // the endpoint
            type : "POST", // http method
            data: {
                device: $('#id_device').val(),
                feature: $('#id_feature').val(),
                summary: $('#id_summary').val(),
                steps: $('#id_steps').val(),
                result: $('#id_result').val()
            },

            success : function(response) {
                $('#id_summary').val(''); // remove the value from the input
                $('#id_steps').val(''); // remove the value from the input
                $('#id_result').val(''); // remove the value from the                                                     input
                console.log("success"); // another sanity check
                if (response.summary) {
                    $("#userBugTableBody").append('<tr><td>'+response.summary+'</td><td align="center"><button  class="btn btn-primary" onclick="editBug({{'+response.id+'}})" data-toggle="modal" data-target="#myModal">EDIT</button></td>');
                };
            },
//            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log('Something Went Wrong')
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

     $("#submit-update-bug").on('click', function(event) {
        var idInput = $('input[name="formId"]').val().trim();
        var summaryInput = $('input[name="formSummary"]').val().trim();
        var stepsInput = $('input[name="formSteps"]').val().trim();
        var resultInput = $('input[name="formResult"]').val().trim();
        console.log(summaryInput)
        console.log(stepsInput)
        console.log(resultInput)
        $.ajax({
            url : "update/", // the endpoint
            type : "POST", // http method
            data: {
                    'id': idInput,
                    'summary': summaryInput,
                    'steps': stepsInput,
                    'result': resultInput
            },
            success : function(response) {
                console.log("Executed this")
                console.log(response)
                if (bug.summary) {
                      $("#userBugTableBody #bug-" + bug.id).children(".bugSummary").each(function() {
                        var attr = $(this).attr("summary");
                        $(this).text(bug.summary);
                        });
                    }
            },
//            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log("Some Error was here")
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
        });



    function updateToUserTable(bug){
        $("#userBugTableBody #bug-" + bug.id).children(".bugSummary").each(function() {
            var attr = $(this).attr("summary");
            $(this).text(bug.summary);
          });
    }
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});



