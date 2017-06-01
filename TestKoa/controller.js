//处理router的注册逻辑

const fs = require('fs');

//注册的具体逻辑
function addMapping(router, mapping) {
    for (var url in mapping) {
        
        //var url = urlMap[0];
        //var register = urlMap[1];
        //console.log(url + " " + mapping[url]);
        if (url.startsWith('GET ')) {
            var path = url.substring(4);
            router.get(path, mapping[url]);
        } else if (url.startsWith('POST ')) {
            var path = url.substring(5);
            router.post(path, mapping[url]);
        }
    }
};

//遍历controllers包里面的.js文件，并分别调用router注册
function addControllers(router, dir) {
    fs.readdirSync(__dirname + '/' + dir)
    .filter((f) => {
        return f.endsWith('.js');
    }).forEach((f) => {
        console.log(__dirname + '/' + dir + '/' + f);
        let mapping = require(__dirname + '/' + dir + '/' + f);
        addMapping(router, mapping);
    })
};

module.exports = function(dir) {
    let controllerDir = dir || 'controllers';
    let router = require('koa-router')();
    addControllers(router, controllerDir);
    return router.routes();
};