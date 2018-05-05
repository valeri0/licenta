
// url for calling the api of the application
var APP_URL = "http://127.0.0.1:5000/";

function httpGetAsync(theUrl, callback,source_code)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    };
    xmlHttp.open("POST", theUrl, true); // true for asynchronous
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(JSON.stringify({'code':source_code}));
}


function render_output_to_console(respone_from_server){
    var _json = JSON.parse(respone_from_server);

    // succesfully executed
    if(_json.code == 500){

        output_console.style.color='red';
        output_console.value = _json.message;

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
        output_console.value = String(_json.message);
    }
}

var editor = ace.edit("editor");
editor.setTheme("ace/theme/chaos");
editor.setShowPrintMargin(false);
editor.session.setMode("ace/mode/python");
document.getElementById('editor').style.fontSize='14px';

var output_console = document.getElementById('console');

document.getElementById("test-button").addEventListener("click",function(){


    editor.getSession().setAnnotations([{}]);
    output_console.classList.add('loading');
    output_console.value='Loading';


    httpGetAsync(APP_URL+"code/test",function (response){

        render_output_to_console(response);
    },
        editor.getValue());

    });