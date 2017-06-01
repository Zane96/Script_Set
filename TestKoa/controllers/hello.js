//处理Hello页面的URL

var hello = async function hello_fn(ctx, next) {
    var name = ctx.params.name;
    ctx.response.body = `<h1>Hello, ${name}!</h1>`;
}

//抛出
module.exports = {
    'GET /hello/:name' : hello
};