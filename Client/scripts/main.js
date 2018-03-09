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

buttonListener = function(){addParagraph();};

//var knapp = document.querySelector('button');
//knapp.addEventListener('click',buttonListener);

function addParagraph(){
    var newPara = document.createElement('p');
    newPara.textContent = "You clicked!";
    document.body.appendChild(newPara)
}



function externalResource() {
    
}




//AAAAAAAJJJJJJJAAAAAAXXXXXX
//Creating XMLHttpRequest object. 


var xhttp = new XMLHttpRequest();
xhttp.open("GET","http://localhost:8000/things",true);
console.log(xhttp.readyState);
xhttp.send();
console.log(xhttp.readyState);
var responsText = xhttp.responseText;
console.log(responsText);
para.textContent = responsText;