//Pet数据表的DAO类

const sequelize = require('./db_helper').sequelize;
const Sequelize = require('./db_helper').Sequelize;
const now = Date.now();

var user = sequelize.define('user', {
        id: {
            type: Sequelize.STRING(50),
            primaryKey: true
        },
        name: Sequelize.STRING(10),
        gender: Sequelize.STRING(10),
        location: Sequelize.STRING(10),
        school: Sequelize.STRING(10),
        subject: Sequelize.STRING(15),
        followees: Sequelize.INTEGER,
        followers: Sequelize.INTEGER,
        agrees: Sequelize.INTEGER,
        thanked: Sequelize.INTEGER,
        intro: Sequelize.STRING(50)
        }, 
    {
        timestamps: false
});

//find
var findUser = async (userId) => {
    var userData = await user.findOne({
        where : {id : userId}
    })

    console.log(`find user is ${userData}------`);
    return userData;
};

module.exports = {
    findUser : findUser
}