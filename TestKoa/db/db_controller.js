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

var Pet = sequelize.define('pet', {
        id: {
            type: Sequelize.STRING(50),
            primaryKey: true
        },
        name: Sequelize.STRING(100),
        gender: Sequelize.BOOLEAN,
        birth: Sequelize.STRING(10),
        createdAt: Sequelize.BIGINT,
        updatedAt: Sequelize.BIGINT,
        version: Sequelize.BIGINT
        }, 
    {
        timestamps: false
});

module.exports = {
    'pet' : Pet
};