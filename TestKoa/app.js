// 导入koa，和koa 1.x不同，在koa2中，我们导入的是一个class，因此用大写的Koa表示:
const Koa = require('koa');
const controller = require('./controller');
const bodyParser = require('koa-bodyparser');
const app = new Koa();


app.use(async (ctx, next) => {
    console.log('Process at ' + ctx.request.method + ' ' + ctx.request.url);
    await next();
});


// 在端口3000监听:
app.use(bodyParser());
app.use(controller());

app.listen(8080);

console.log('app started at port 8080...');
