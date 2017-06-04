// 导入koa，和koa 1.x不同，在koa2中，我们导入的是一个class，因此用大写的Koa表示:
const Koa = require('koa');
const controller = require('./controller');
const bodyParser = require('koa-bodyparser');
const app = new Koa();
const pet_db = require(__dirname + '/' + 'db' + '/' + 'pet_dao');
const WebSocket = require('ws');
const WebSocketServer = WebSocket.Server;
const webSocket = require('./websocket');


const wss = new WebSocketServer({
    port : 3000
});

webSocket.wssConnection(wss);
const ws = new WebSocket('ws://127.0.0.1:3000');
webSocket.wsOpen(ws);

app.use(async (ctx, next) => {
    console.log('Process at ' + ctx.request.method + ' ' + ctx.request.url);
    await next();
});

// 在端口3000监听:
app.use(bodyParser());
app.use(controller());

//pet_db.insert;
pet_db.findAll();

//app.listen(8080);
console.log('app started at port 8080...');


//ws.wssConnection;
//ws.wsOpen;
