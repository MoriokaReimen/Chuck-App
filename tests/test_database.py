from chuck_norris import database

def test_database():
    entry = database.Entry('hogehoge')
    entry.attachments = ['fuga', 'buzz']
    entry2 = database.Entry('fugafuga')
    entry2.attachments = ['fuga2', 'buzz2']
    db = database.DataBase()
    db.add(entry)
    db.add(entry2)
    db.add(entry)
    db.add(entry2)
    db.commit()
    found = db.get_all()
    print(found)

