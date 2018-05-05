
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


var editor = ace.edit("editor");
editor.setTheme("ace/theme/chaos");
editor.setShowPrintMargin(false);
editor.session.setMode("ace/mode/python");
document.getElementById('editor').style.fontSize='14px';

var output_console = document.getElementById('console');

document.getElementById("test-button").addEventListener("click",function(){
    httpGetAsync(APP_URL+"code/test",function (response){
        output_console.value = response;
    },
        editor.getValue());

    });