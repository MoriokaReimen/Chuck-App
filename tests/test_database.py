# -*- coding: utf-8 -*-
from driver import DataBase
import os
from datetime import datetime

def test_database():
    if os.path.isfile('database.db') :
        os.remove('database.db')

    entry1 = DataBase.Entry()
    entry1.contents = 'hogehoge1'
    entry1.attachments = ['fuga1', 'buzz1']
    entry1.time_sent = datetime.now()
    entry1.title = 'mail1'
    entry1.sender = 'mail1'
    entry1.receiver = 'mail1'

    entry2 = DataBase.Entry()
    entry2.contents = 'hogehoge2'
    entry2.attachments = ['fuga2', 'buzz2']
    entry2.time_sent = datetime.now()
    entry2.title = 'mail2'
    entry2.sender = 'mail2'
    entry2.receiver = 'mail2'

    entry3 = DataBase.Entry()
    entry3.contents = 'hogehoge3'
    entry3.attachments = ['fuga3', 'buzz3']
    entry3.time_sent = datetime.now()
    entry3.title = 'mail3'
    entry3.sender = 'mail3'
    entry3.receiver = 'mail3'

    entry4 = DataBase.Entry()
    entry4.contents = 'hogehoge4'
    entry4.attachments = ['fuga4', 'buzz4']
    entry4.time_sent = datetime.now()
    entry4.title = 'mail4'
    entry4.sender = 'mail4'
    entry4.receiver = 'mail4'

    db = DataBase.DataBase('database.db')
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

