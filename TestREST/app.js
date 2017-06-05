const Koa = require('koa');
const controller = require('./controller');
const bodyParser = require('koa-bodyparser');
const rest = require('./rest');
const app = new Koa();

app.use(async (ctx, next) => {
    console.log(`API now is ${ctx.request.method} ${ctx.request.url}`);
    await next();
});

app.use(bodyParser());
app.use(rest.restify());
app.use(controller());

app.listen(3000);

console.log('Server is listening at 3000');
