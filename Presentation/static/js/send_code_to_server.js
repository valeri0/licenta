
// url for calling the api of the application
var APP_URL = "http://127.0.0.1:5000/";

function set_editor_options(editor){

    editor.setTheme("ace/theme/chaos");
    editor.setShowPrintMargin(false);
    editor.session.setMode("ace/mode/python");
    document.getElementById('editor').style.fontSize='14px';
}

function httpGetAsync(theUrl, callback,source_code,id) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    };
    xmlHttp.open("POST", theUrl, true); // true for asynchronous
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(JSON.stringify({'code':source_code,'id':id}));
}

function render_output_to_console(respone_from_server){
    var _json = JSON.parse(respone_from_server);

    // succesfully executed
    if(_json.code == 500){

        output_console.style.color='red';
        output_console.value = "Output: "+_json.message;

        //Error at:  line 2
        var line_number = parseInt(_json.message[16])-1;

        editor.getSession().setAnnotations([{
              row: line_number,
              column: 0,
              type: "error"
        }]);
    }
    // error at execution
    else {
        output_console.style.color='green';
        output_console.value = "Output: "+String(_json.message);
    }
}

function lesson_test_code(lesson_id){

    editor.getSession().setAnnotations([{}]);
    output_console.classList.add('loading');
    output_console.value='Loading';


    httpGetAsync(APP_URL+"lesson/test",function (response){

        render_output_to_console(response);
    },
        editor.getValue(),lesson_id);

}

function lesson_submit_code(lesson_id){

    editor.getSession().setAnnotations([{}]);
    output_console.classList.add('loading');
    output_console.value='Loading';


    httpGetAsync(APP_URL+"lesson/submit",function (response){

        render_output_to_console(response);
    },
        editor.getValue(),lesson_id);
}


function exercise_test_code(exercise_id){

    editor.getSession().setAnnotations([{}]);
    output_console.classList.add('loading');
    output_console.value='Loading';


    httpGetAsync(APP_URL+"exercise/test",function (response){

        render_output_to_console(response);
    },
        editor.getValue(),exercise_id);

}

function exercise_submit_code(exercise_id){

    editor.getSession().setAnnotations([{}]);
    output_console.classList.add('loading');
    output_console.value='Loading';


    httpGetAsync(APP_URL+"exercise/submit",function (response){

        render_output_to_console(response);
    },
        editor.getValue(),exercise_id);
}




var editor = ace.edit("editor");
set_editor_options(editor);
var output_console = document.getElementById('console');
