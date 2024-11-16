import sqlite3
from dataclasses import dataclass

@dataclass(init=False)
class Entry:
    contents : str
    attachments : list[str]
    id : int = 0

    def __init__(self, contents :str, id :int = 0):
        self.id = id
        self.contents = contents
        self.attachments = list()

def factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class DataBase:
    def __init__(self, db_name : str = 'database.db'):
        self._data_base = sqlite3.connect(db_name)
        self._data_base.row_factory = factory
        self._cur = self._data_base.cursor()
        self._cur.execute(
            '''
                CREATE TABLE IF NOT EXISTS mail(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contents TEXT NOT NULL)
            ''')
        self._cur.execute(
            '''
                CREATE TABLE IF NOT EXISTS attachment(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mail_id INTEGER NOT NULL,
                attachment TEXT NOT NULL)
            ''')
        self._data_base.commit()

    def commit(self):
        self._data_base.commit()

    def add(self, entry : Entry) -> bool:
        self._cur.execute(
        '''
            INSERT INTO mail(contents)
            VALUES (:contents)
            RETURNING id
        ''', {'contents' : entry.contents})
        mail_id = self._cur.fetchone()['id']

        for attachment in entry.attachments:
            self._cur.execute(
            '''
                INSERT INTO attachment(mail_id, attachment)
                VALUES (:mail_id, :attachment)
            ''', {'mail_id' : mail_id, 'attachment': attachment})

    def query(self, key : str, value : str):
        sql = f'SELECT * FROM mail WHERE {key} LIKE \'%{value}%\';' 
        mails = self._cur.execute(sql).fetchall()

        ret = list()
        for mail in mails:
            entry = Entry(**mail)
            entry.attachments = self._get_attachments(entry.id)
            ret.append(entry)
        return ret

    def get_all(self) -> list[Entry]:
        sql = 'SELECT * FROM mail;' 
        mails = self._cur.execute(sql).fetchall()

        ret = list()
        for mail in mails:
            entry = Entry(**mail)
            entry.attachments = self._get_attachments(entry.id)
            ret.append(entry)
        return ret

    def _get_attachments(self, id : int) -> list[str]:
        sql = f'SELECT * FROM attachment WHERE mail_id ={id};' 
        attachments = self._cur.execute(sql).fetchall()
        ret = list()
        for attachment in attachments:
            print(attachment)
            ret.append(attachment['attachment'])
        return ret

