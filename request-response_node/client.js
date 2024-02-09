const http = require('http');

console.log('send request to server every 3s')
setInterval(function(){
    http.get({
        host: 'server', 
        path: '/',
        port: 5544
    }, function(resp){
        resp.on('data', function(ev){
            console.log('event: ' + ev)
        })
    })
}, 3000);