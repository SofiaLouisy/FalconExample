//Testa min kontakt
var head = document.querySelector('h1')
head.textContent = 'Hi there!'

//Testa kontakt igen. 
var para = document.querySelector('p');
para.textContent = 'Hi again!';
$("p").text("JQuery works");

//ButtonListeners
document.querySelector('#b1').onclick = stopInterval;
document.querySelector('#b2').onclick = colorPostRequest;

//-----Functions-----

function addParagraph(content){
    var newPara = document.createElement('p');
    newPara.textContent = content;
    newPara.innerHTML = newPara.innerHTML.replace('\n', '<br>');
    document.body.appendChild(newPara);
};

function externalResource() {
    $.getJSON("http://localhost:8000/hello",{},function(data){
        console.log(data);
        
        //greeting = {"greeting":'Hello world /Server!'}
        //console.log(JSON.stringify(greeting));
        //var myJSONobject = jQuery.parseJSON(data);//JSON.parse(data);
        addParagraph(data.greeting);
    })
}

function greetingPostRequest() {
    JSONstring = JSON.stringify({'greeting':'Hello server! /postRequest'})
    console.log(JSONstring)
    $.post("http://localhost:8000/hello",JSONstring,function(data){
        console.log(data);
        addParagraph((data.requestGreeting+"\n"+ data.greeting));
    })
}

//Jag skickar vilken nuvarande färg jag har
//servern ger mig den nya färgen
//Jag måste hitta hur jag får tag på nuvarande färgen
function colorPostRequest() {
    JSONstring = JSON.stringify({'color':document.querySelector('html').style.backgroundColor})
    $.post("http://localhost:8000/color",JSONstring,function(data){
        document.querySelector('html').style.backgroundColor = data.color;
    })
}

interval = setInterval(colorPostRequest, 1000);

function stopInterval() {
    clearInterval(interval);
    addParagraph('You will never get it back!!');
}