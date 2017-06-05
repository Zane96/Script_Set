//Pet数据表的DAO类

var sequelize = require('./db_controller').sequelize;
var now = Date.now();

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

//insert
var insert = Pet.create({
    id: 'g-' + now,
    name: 'Zane',
    gender: false,
    birth: '2007-07-07',
    createdAt: now,
    updatedAt: now,
    version: 0
}).then(function (p) {
    console.log('created.' + JSON.stringify(p));
}).catch(function (err) {
    console.log('failed: ' + err);
});

//find
var findAll = async () => {
    var pets = await Pet.findAll({
        where : {
            name : 'Zane'
        }
    })
    console.log(`find ${pets.length} pets:`);
    for (let p of pets) {
        console.log('result------ ' + JSON.stringify(p));
    }
    return pets;
};

//save
var save = async () => {
    var pets = findAll();
    for(let p of pets) {
        p.version ++;
        await p.save();

        if (p.version === 3) {
            await p.destory();
            console.log(`${p.name} was destroyed.`);
        }
    }
};

module.exports = {
    insert : insert,
    findAll : findAll,
    save : save
};