# -*- coding: utf-8 -*-
from driver import DataBase
import os

def test_database():
    if os.path.isfile('test.db') :
        os.remove('test.db')

    entry1 = DataBase.Entry()
    entry1.contents = 'hogehoge1'
    entry1.attachments = ['fuga1', 'buzz1']

    entry2 = DataBase.Entry()
    entry2.contents = 'hogehoge2'
    entry2.attachments = ['fuga2', 'buzz2']

    entry3 = DataBase.Entry()
    entry3.contents = 'hogehoge3'
    entry3.attachments = ['fuga3', 'buzz3']

    entry4 = DataBase.Entry()
    entry4.contents = 'hogehoge4'
    entry4.attachments = ['fuga4', 'buzz4']

    db = DataBase.DataBase('test.db')
    assert db.add(entry1)
    assert not db.add(entry1)

    assert db.add(entry2)
    assert not db.add(entry2)

    assert db.add(entry3)
    assert not db.add(entry3)

    assert db.add(entry4)
    assert not db.add(entry4)

    db.commit()
    found = db.get_all()
    print(found)

