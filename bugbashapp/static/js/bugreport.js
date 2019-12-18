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