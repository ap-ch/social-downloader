db.users.drop();
db.users.createIndex({ "email": 1 }, { unique: true })