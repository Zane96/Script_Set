//数据库连接操作module

var Sequelize = require('sequelize');
var config = require('./config');

var sequelize = new Sequelize(config.database, config.username, config.password, {
    host : config.host,
    dialect : 'mysql',
    pool: {
        max: 5,
        min: 0,
        idle: 30000
    }
});

module.exports = {
    sequelize : sequelize
};