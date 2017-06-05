//api的响应逻辑

const user = require('../db/user');
const rest = require('../rest');

var getUser = async (ctx, next) => {
    var id = ctx.params.id;
    var userData = await user.findUser(id);
    console.log('userData: ' + JSON.stringify(userData));
    if (userData) {
        ctx.rest(JSON.stringify(userData));
    } else {
        throw new rest.APIError("user:not found", "userinfo not found by id");
    }
};

module.exports = {
    'GET /api/user/:id' : getUser
};
