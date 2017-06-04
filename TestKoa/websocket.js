
var wssConnection = function(wss) {
    wss.on('connection', (ws) => {
        console.log('Server Connection-------');
        ws.on('message', (message) => {
            console.log(`Server reciver message: ${message}`);
            ws.send(`ECHO: ${message}`, (err) => {
                if(err) {
                    console.log(`Server error: ${err}`);
                }
            })
        })
    });
};

var wsOpen = function(ws) {
    ws.on('open', () => {
        console.log('Client Open----------------');
        ws.send('Hello, SB!');
    });

    ws.on('message', (message) => {
        console.log(`Client reciver message: ${message}`);
    });
};

module.exports = {
    wssConnection : wssConnection,
    wsOpen : wsOpen
};