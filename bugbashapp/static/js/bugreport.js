function editBug(bug_id) {
      console.log('editBugWAS FOUND!!!!!!!!!!!')
      console.log(bug_id)
      if (bug_id) {
        tr_id = "#bug-" + bug_id;
        summary = $(tr_id).find(".id_summary").text();
        $('#bug-id').val(bug_id);
        $('#id_summary').val(summary);
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