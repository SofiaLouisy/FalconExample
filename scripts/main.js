

//Testa min kontakt
var head = document.querySelector('h1')
head.textContent = 'Hi there!'

//Testa kontakt igen. 
//Denna måste vara framför io om det ska ske i uppstart
var para = document.querySelector('p');
para.textContent = 'Hi again!';

//connecta med servern
var socket = io('http://localhost');
socket.on('colors', function(data) {
    console.log(data);
    socket.emit('my other event', {my: 'data'})
});