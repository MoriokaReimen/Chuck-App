import sqlite3
from dataclasses import dataclass, field
import hashlib

@dataclass
class Entry:
    contents : str = ''
    attachments : list[str] = field(default_factory = list)
    title : str = ''
    sender : str = ''
    receiver : str = ''

    def hash(self) -> str:
        hasher = hashlib.sha256()
        hasher.update(self.contents.encode())
        hasher.update(self.title.encode())
        hasher.update(self.sender.encode())
        hasher.update(self.receiver.encode())
        return hasher.hexdigest()

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
                hash TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                sender TEXT NOT NULL,
                receiver TEXT NOT NULL,
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
        hash = entry.hash()

        # Check value is exists?
        found = self.query(key = 'hash', value = hash)
        if found :
            return False

        # If value is not exists in table add entry
        self._cur.execute(
        '''
            INSERT INTO mail(hash, title, contents, sender, receiver)
            VALUES (:hash, :title, :contents, :sender, :receiver)
            RETURNING id
        ''', {'hash' : hash,
              'contents' : entry.contents,
              'title' : entry.title,
              'sender' : entry.sender,
              'receiver' : entry.receiver,
             })
        mail_id = self._cur.fetchone()['id']

        for attachment in entry.attachments:
            self._cur.execute(
            '''
                INSERT INTO attachment(mail_id, attachment)
                VALUES (:mail_id, :attachment)
            ''', {'mail_id' : mail_id, 'attachment': attachment})
        return True

    def query(self, key : str, value : str):
        sql = f'SELECT * FROM mail WHERE {key} LIKE \'%{value}%\';'
        mails = self._cur.execute(sql).fetchall()

        ret = []
        for mail in mails:
            entry = Entry()
            entry.contents = mail['contents']
            entry.title = mail['title']
            entry.sender = mail['sender']
            entry.receiver = mail['receiver']
            entry.attachments = self._get_attachments(mail['id'])
            ret.append(entry)
        return ret

    def get_all(self) -> list[Entry]:
        sql = 'SELECT * FROM mail;'
        mails = self._cur.execute(sql).fetchall()

        ret = []
        for mail in mails:
            entry = Entry()
            entry.contents = mail['contents']
            entry.title = mail['title']
            entry.sender = mail['sender']
            entry.receiver = mail['receiver']
            entry.attachments = self._get_attachments(mail['id'])
            ret.append(entry)
        return ret

    def _get_attachments(self, id : int) -> list[str]:
        sql = f'SELECT * FROM attachment WHERE mail_id ={id};'
        attachments = self._cur.execute(sql).fetchall()
        ret = []
        for attachment in attachments:
            ret.append(attachment['attachment'])
        return ret

