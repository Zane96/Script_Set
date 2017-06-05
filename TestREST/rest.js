//封装API的一些处理，一个中间件

//错误封装
var APIError = (code, message) => {
    var code = code || 'unknow error';
    var message = message || '';
};

//给ctx绑定一个方便初始化的函数
var restify = (pathPrefix) => {
    pathPrefix = pathPrefix || '/api/';
    return async (ctx, next) => {
        if (ctx.request.path.startsWith(pathPrefix)) {
            ctx.rest = (data) => {
                //处理API
                ctx.response.type = 'application/json';
                ctx.response.body = data;
            }; 
            try {
                //等待下一个中间件的thowers的error
                await next();
            }catch (e) {
                //进行错误处理
                console.log("APIError----------");
                ctx.response.status = 400;
                ctx.response.type = 'application/json';
                ctx.response.body = {
                    code : e.code || 'unkown error',
                    message : e.message || '' 
                };
            }
        }else{
            //如果不是处理
            await next();
        }
    };
};

module.exports = {
    APIError : APIError,
    restify : restify
}