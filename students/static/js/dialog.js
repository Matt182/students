function Update(clicked_id) {
        (function() {
            var dialog = document.getElementById('dialog_form');
            dialog.show();
            document.getElementById('old').value = clicked_id;
            document.getElementById('exit').onclick = function() {
                dialog.close();
            };
        })();
    };