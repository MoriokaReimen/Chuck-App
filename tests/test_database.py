# -*- coding: utf-8 -*-
from driver import DataBase

def test_database():
    entry = DataBase.Entry('hogehoge')
    entry.attachments = ['fuga', 'buzz']
    entry2 = DataBase.Entry('fugafuga')
    entry2.attachments = ['fuga2', 'buzz2']
    db = DataBase.DataBase()
    db.add(entry)
    db.add(entry2)
    db.add(entry)
    db.add(entry2)
    db.commit()
    found = db.get_all()
    print(found)

