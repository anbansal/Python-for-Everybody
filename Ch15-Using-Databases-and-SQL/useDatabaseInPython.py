from sqlDatabase import sqlDatabase

if __name__ == '__main__':
    tableName = 'Tracks'
    newDB = sqlDatabase(tableName)
    cmd = 'INSERT INTO ' + tableName + ' (title, plays) VALUES ("Thunderstruck", 20)'
    newDB.insertIntoDB(cmd)
    cmd = 'INSERT INTO ' + tableName + ' (title, plays) VALUES ("my way", 15)'
    newDB.insertIntoDB(cmd)
    cmd = 'SELECT title,plays from ' + tableName
    newDB.showDB(cmd)
    newDB.delDB()
