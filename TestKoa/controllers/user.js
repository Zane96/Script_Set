//处理user逻辑的URL

var index = (ctx, next) => {
    ctx.response.body = `<h1>Index</h1>
        <form action="/signin" method="post">
            <p>Name: <input name="name"></p>
            <p>Password: <input name="password" type="password"></p>
            <p><input type="submit" value="Submit"></p>
        </form>`;
};

var signin = (ctx, next) => {
    var name = ctx.request.body.name || '';
    var password = ctx.request.body.password || '';

    if(name === 'zane' && password === '123') {
        ctx.response.body = `Hello, ${name}!`;
    } else {
        ctx.response.head = 403;
        ctx.response.body = '<h1>403</h1>';
    }
};

//抛出
module.exports = {
    'GET /' : index,
    'POST /signin' : signin
};