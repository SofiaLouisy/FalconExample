//<script src = scripts/main.js></script>
//<script src = "https://localhost:8000/things"></script>

// 1. Load the JavaScript client library.
//gapi.load('client', start);
  
//Testa min kontakt
var head = document.querySelector('h1')
head.textContent = 'Hi there!'

//Testa kontakt igen. 
//Denna måste vara framför io om det ska ske i uppstart
var para = document.querySelector('p');
para.textContent = 'Hi again!';

buttonListener = function(){externalResource();};

var knapp = document.querySelector('button');
knapp.addEventListener('click',buttonListener);

function addParagraph(content){
    var newPara = document.createElement('p');
    newPara.textContent = content;
    document.body.appendChild(newPara);
};

$("p").text("JQuery works");

function externalResource() {
    $.getJSON("http://localhost:8000/hello",{},function(data){
        console.log(data);
        
        //greeting = {"greeting":'Hello world /Server!'}
        //console.log(JSON.stringify(greeting));
        //var myJSONobject = jQuery.parseJSON(data);//JSON.parse(data);
        addParagraph(data.greeting);
    })

}
