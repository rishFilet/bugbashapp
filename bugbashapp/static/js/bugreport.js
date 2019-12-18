function editBug(bug_id) {
      console.log('editBugWAS FOUND!!!!!!!!!!!')
      console.log(bug_id)
      if (bug_id) {
        tr_id = "#bug-" + bug_id;
        summary = $(tr_id).find(".id_summary").text();
        $('#bug-id').val(bug_id);
        $('#id_summary').val(summary);

        $.ajax({
            url : "update/", // the endpoint
            type : "GET", // http method
            data: {
                id: bug_id
            },

            success : function(response) {
                $('#form-name').val(response.summary);
                $('#form-address').val(response.steps);
                $('#form-result').val(response.result);
                console.log("success"); // another sanity check
            },
//            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log('Something Went Wrong')
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
      }
    }

function deleteBug(id) {
  var action = confirm("Are you sure you want to delete this Bug?");
  if (action != false) {
    $.ajax({
        url : "delete/", // the endpoint
        type : "POST", // http method
        data: {
            'id': id,
        },
        success: function (data) {
            if (data.deleted) {
              $("#userBugTable #bug-" + id).remove();
            }
        }
    });
  }
}
