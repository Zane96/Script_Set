//Pet数据表的DAO类

var Pet = require('./db_controller').Pet;
var now = Date.now();

//insert

// var insert = async () => {
//     var dog = await Pet.create({
//         id: 'd-' + now,
//         name: 'Zane',
//         gender: false,
//         birth: '2008-08-08',
//         createdAt: now,
//         updatedAt: now,
//         version: 0
//     });
//     console.log('created: ' + JSON.stringify(dog));
// };
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